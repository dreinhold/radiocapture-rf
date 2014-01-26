#!/usr/bin/env python

#(C) 2013 - Matt Mills
#Configuration File Structure (channel definitions)
#Changes:
# 4/28/2013 - Initial Creation
class rc_config:
	def __init__(self):

		self.sources = {
			0:{
                                'type': 'bladerf',
                                'center_freq': 855500000,
                                'samp_rate': 10666666,
                                'rf_gain': 2,
				'bb_gain': 18
                        },
			1:{
                                'type': 'usrp',
                                'device_addr': "recv_frame_size=24576,num_recv_frames=512,serial=E2R10Z3B1",
                                #'device_addr': "serial=E2R10Z3B1",
                                'otw_format': 'sc16',
                                'args': '',
                                'center_freq': 771500000,
                                'samp_rate': 10666666,
                                'rf_gain': 3
			}
		}
                self.systems = {
                        0: { #Adams County Simulcast (Denver Metro)	3	22
                                'type': 'p25',
                                'id': 0xbee07,#3022,
                                'default_control_channel': 0,
                                'channels': {
					0: 770106250,
					1: 770356250,
					2: 770606250,
					3: 771106250,
					4: 771481250,
					5: 771731250,
					6: 772156250,
					7: 772493750,
					8: 772731250,
					9: 772743750,
					10: 772981250,
					11: 772993750
                                }
                        },
                        1: { #Arapahoe Admin (Denver Metro)	1	1
                                'type': 'p25',
                                'id': 0xbee07,#1001,
                                'default_control_channel': 0,
                                'channels': {
					0: 851225000,
					1: 851775000,
					2: 852100000,
					3: 852362500,
					4: 852937500,
					5: 853237500,
					6: 853437500,
					7: 853662500,
					8: 854862500,
					9: 856687500,
					10: 858387500

                                }
                        },
                        2: { #Auraria Campus (Denver Metro)	1	70
                                'type': 'p25',
                                'id': 0xbee07,#1070,
                                'default_control_channel': 0,
                                'channels': {
					0: 769156250,
					1: 769406250,
					2: 769656250,
					3: 769906250,
					4: 770156250,
					5: 770406250,
					6: 770656250,
					7: 770906250,
					8: 773031250,
					9: 773281250,
					10: 773531250,
					11: 773781250

                                }
                        },
                        3: { #Chevron Plaza Tower (Denver Metro)	1	64
                                'type': 'p25',
                                'id': 0xbee07,#1064,
                                'default_control_channel': 0,
                                'channels': {
					0: 769256250,
					1: 771556250,
					2: 772006250,
					3: 772818750,
					4: 773131250,
					5: 773681250,
					6: 851787500,
					7: 852875000,
					8: 853837500,
					9: 857687500,
					10: 858062500,
					11: 858512500,
					12: 858687500,
					13: 859037500,
					14: 859512500,
					15: 859912500

                                }
                        },
                        4: { #Denver TX (Denver Metro)	1	20
                                'type': 'p25',
                                'id': 0xbee07,#1020,
                                'default_control_channel': 0,
                                'channels': {
					0: 770281250,
					1: 772556250,
					2: 773906250,
					3: 774306250,
					4: 774556250,
					5: 774806250,
					6: 851437500,
					7: 852362500,
					8: 852562500,
					9: 852812500,
					10: 853112500,
					11: 853700000

                                }
                        },
                        5: { #DRDC CF	1	9
                                'type': 'p25',
                                'id': 0xbee07,#1009,
                                'default_control_channel': 0,
                                'channels': {
					0: 851150000,
					1: 851950000,
					2: 852700000,
					3: 853475000,
					4: 853675000,
					5: 853962500

                                }
                        },
                        6: { #Fort Lupton	3	55
                                'type': 'p25',
                                'id': 0xbee07,#3055,
                                'default_control_channel': 0,
                                'channels': {
					0: 770256250,
					1: 771006250,
					2: 771256250,
					3: 771543750,
					4: 771843750,
					5: 772093750,
					6: 772393750,
					7: 773168750,
					8: 773418750

                                }
                        },
                        7: { #Lookout Mountain (Denver Metro)	1	8
                                'type': 'p25',
                                'id': 0xbee07,#1008,
                                'default_control_channel': 0,
                                'channels': {
					0: 851112500,
					1: 851400000,
					2: 851487500,
					3: 851687500,
					4: 851987500,
					5: 852037500,
					6: 852200000,
					7: 852412500,
					8: 852487500,
					9: 853062500,
					10: 853412500,
					11: 853487500,
					12: 853775000,
					13: 854162500,
					14: 855437500,
					15: 855837500,
					16: 856062500,
					17: 856512500,
					18: 857787500
                                }
                        },
                        8: { #State Capitol (Denver Metro)	1	71
                                'type': 'p25',
                                'id': 0xbee07,#1071,
                                'default_control_channel': 0,
                                'channels': {
					0: 769306250,
					1: 769531250,
					2: 769781250,
					3: 770581250,
					4: 771456250,
					5: 772206250,
					6: 773231250,
					7: 773481250,
					8: 774031250,
					9: 774281250,
					10: 774656250,
					11: 774906250
                                }
                        },

		}
		
                del self.systems[1]
                del self.systems[2]
                del self.systems[4]
                del self.systems[6]
                del self.systems[7]
                del self.systems[8]

		del self.systems[3]
		del self.systems[5]
