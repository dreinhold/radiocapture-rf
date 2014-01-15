#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Moto Smartzone Test1
# Generated: Thu Oct  4 23:49:39 2012
##################################################

from gnuradio import filter
from gnuradio import gr
from gnuradio import blocks
from gnuradio.filter import firdes

import time
import threading

from logging_receiver import logging_receiver

class scanning_receiver(gr.hier_block2):

	def __init__(self, system, samp_rate, sources, top_block, block_id):

                gr.hier_block2.__init__(self, "scanning_receiver",
                                gr.io_signature(1, 1, gr.sizeof_gr_complex), # Input signature
                                gr.io_signature(0, 0, 0)) # Output signature

		##################################################
		# Variables
		##################################################
		self.tb = top_block
		self.samp_rate = samp_rate
		self.block_id = block_id
		self.system = system
		self.system_id = system['id']
		self.sources = sources
		self.channels = system['channels']
		self.center_freq = sources[system['source']]['center_freq']

		##################################################
		# Threads
		##################################################

		receive_engine = threading.Thread(target=self.receive_engine)
		receive_engine.daemon = True
		receive_engine.start()

		##################################################
		# Blocks
		##################################################

		self.source = self

		self.audio_rate = audio_rate = 12500.0

		channel_rate = audio_rate*1.6
		f1d = int(samp_rate/channel_rate) #filter 1 decimation

		self.prefilter_taps = firdes.low_pass(1.0,samp_rate,(audio_rate/2), (audio_rate*0.3), firdes.WIN_HAMMING)
		self.prefilter = filter.freq_xlating_fir_filter_ccc(f1d, self.prefilter_taps, 0, samp_rate)
		self.complex_to_mag_squared = blocks.complex_to_mag_squared(1)
		self.probe = blocks.probe_signal_f()
	
		##################################################
		# Connections
		##################################################
		self.connect(self.source, self.prefilter, self.complex_to_mag_squared, self.probe)

	def call_progress(self, freq):
		self.tb.ar_lock.acquire()
		free_ar = []

		for r in self.tb.active_receivers:
			if(r.in_use == False):
				free_ar.append(r)
			if(r.cdr != {} and r.cdr['system_id'] == self.system['id'] and r.cdr['system_channel_local'] == freq and r.in_use == True):
				r.activity()
				self.tb.ar_lock.release()
				return None
		#new call, either find empty receiver or create a new one, then insert into call table
		allocated_receiver = False

		for r in free_ar:
			if abs(r.center_freq-freq) < (self.samp_rate/2):
				allocated_receiver = r
				center = r.center_freq
				break
		if allocated_receiver == False:
			allocated_receiver = logging_receiver(self.samp_rate)
			center = self.tb.connect_channel(freq, allocated_receiver)
			#I have no idea why this is here:
			#first_probe = self.probe.level()
			#print 'time in: %s' % (time.time())
			#while self.probe.level() == first_probe:
			#	pass
			#print 'time out: %s' % (time.time())

			self.tb.active_receivers.append(allocated_receiver)

		allocated_receiver.tuneoffset(freq, self.center_freq)
		allocated_receiver.set_codec_p25(False)
		allocated_receiver.set_codec_provoice(False)
			
		cdr = {
			'system_id': self.system['id'],
			'system_group_local': freq,
			'system_user_local': 0,
			'system_channel_local': freq,
			'type': 'group',
			'center_freq': self.center_freq
		}

		allocated_receiver.open(cdr, self.audio_rate)
		self.tb.ar_lock.release()
		
###################################################################################################
	def receive_engine(self):
		print 'scanning_receiver: receive_engine() startup'
		print self.channels
		time.sleep(3)
		while(True):
			for key,freq in self.channels.iteritems():
				self.prefilter.set_center_freq(freq-self.center_freq)
				#print 'tune %s' % (self.center_freq-freq)
				time.sleep(0.010)
				#if self.probe.level() > 3.0e-6:
				#	self.call_progress(freq)
				#	print '*Freq: %s Level: %s' % (freq, self.probe.level())
				#elif self.probe.level() > 9.0e-7:
				#	print ' Freq: %s Level: %s' % (freq, self.probe.level())
				#else:
				#	print ' Freq: %s Level: %s' % (freq, self.probe.level())
