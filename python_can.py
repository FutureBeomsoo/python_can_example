# import can

# with can.Bus() as bus:

#     msg = can.Message(
#         arbitration_id=0xC0FFEE,
#         data=[0, 25, 0, 1, 3, 1, 4, 1],
#         is_extended_id=True
#     )
#     try:
#         bus.send(msg)
#         print(f"Message sent on {bus.channel_info}")

#         for msg in bus:
#             print(msg.data)

#     except can.CanError:
#         print("Message NOT sent")


############################################################

# import can

# filters = [
#     {"can_id": 0x451, "can_mask": 0x7FF, "extended": False},
#     {"can_id": 0xA0000, "can_mask": 0x1FFFFFFF, "extended": True},
# ]

# with can.interface.Bus(channel="vcan0", interface="socketcan", can_filters=filters) as bus:

#     msg = can.Message(
#         arbitration_id=0xC0FFEE,
#         data=[0, 25, 0, 1, 3, 1, 4, 1],
#         is_extended_id=True
#     )
#     try:
#         bus.send(msg)
#         print(f"Message sent on {bus.channel_info}")

#         for msg in bus:
#             print(msg.data)

#     except can.CanError:
#         print("Message NOT sent")


######################################################

# import can

# with can.ThreadSafeBus(interface='socketcan', channel='vcan0') as bus:

#     msg = can.Message(
#         arbitration_id=0xC0FFEE,
#         data=[0, 25, 0, 1, 3, 1, 4, 1],
#         is_extended_id=True
#     )
#     try:
#         bus.send(msg)
#         print(f"Message sent on {bus.channel_info}")

#         # bus.recv()

#         for msg in bus:
#             print(msg.data)

#     except can.CanError:
#         print("Message NOT sent")

########################################################

# import can 

# test = can.Message(data= [1, 2, 3, 4, 5])
# print(test.data)
# print(test.dlc)
# print(test)

# print(can.Message(is_extended_id=False, arbitration_id=100)) # DEC 100 = 0x64  / 6*2^4 + 4 = 100

# example_data = bytearray([1, 2, 3])
# print(can.Message(data=example_data))
# print(can.Message(data=example_data).data)

# m1 = can.Message(data=[0x64, 0x65, 0x61, 0x64, 0x62, 0x65, 0x65, 0x66])
# print(m1)
# print(m1.data)
# m2 = can.Message(data=b'deadbeef')
# print(m2.data)

# example_data = bytearray([65, 66, 67])    # 65 = 0x41 = 'A' / 66 = 0x42 = 'B' 67 = 0x43 = 'C'
# print(can.Message(data=example_data))
# print(can.Message(data=example_data).data)

# m1 = can.Message(data=[0x01, 0x02, 0x03, 0x4])
# print(m1.data)

# m = can.Message(data=[1, 2, 3])
# print(m.dlc)

################################################################################
# import can 

# print(can.Message(is_extended_id=True))
# print(can.Message(is_extended_id=False))

# print(can.Message(is_error_frame=True))
# print(can.Message(is_error_frame=False))

# print(can.Message(is_remote_frame=True))
# print(can.Message(is_remote_frame=False))

# print(can.Message(is_fd=True))
# print(can.Message(is_fd=False))

# print(can.Message(is_rx=True))
# print(can.Message(is_rx=False))

# print(can.Message(bitrate_switch=True))
# print(can.Message(bitrate_switch=False))

# print(can.Message(error_state_indicator=True))
# print(can.Message(error_state_indicator=False))

# m= can.Message(is_extended_id=False,is_error_frame=True,is_remote_frame=True,is_fd=True,is_rx=False,bitrate_switch=True,error_state_indicator=True)
# print(m.__str__())

#################################################################################


# #!/usr/bin/env python

# import time
# import can


# def main():
#     with can.Bus(receive_own_messages=True) as bus:
#         print_listener = can.Printer()

#         can.Notifier(bus, [print_listener])

#         bus.send(can.Message(arbitration_id=1, is_extended_id=True))
#         bus.send(can.Message(arbitration_id=2, is_extended_id=True))
#         bus.send(can.Message(arbitration_id=1, is_extended_id=False))

#         time.sleep(1.0)


# if __name__ == "__main__":
#     main()

####################################################################################


# #################################################

# listener = SomeListener()
# msg = my_bus.recv()

# # now either call
# listener(msg)
# # or
# listener.on_message_received(msg)

# # Important to ensure all outputs are flushed
# listener.stop()

# #################################################


# #!/usr/bin/env python

# import time
# import can

# def main():
#     with can.Bus(receive_own_messages=True) as bus:
#     # with can.Bus() as bus:

#         # RedirectReader Test

#         RedirectReader_listener = can.RedirectReader(can.Bus(interface='socketcan', channel='vcan1'))
#         msg = bus.recv()

#         # now either call
#         RedirectReader_listener(msg)
#         RedirectReader_listener.on_message_received(msg)
#         RedirectReader_listener(can.Message(arbitration_id=0x321, is_extended_id=False, data = bytearray([0x01, 0x02, 0x03]), dlc = 8))
#         RedirectReader_listener.on_message_received(can.Message(arbitration_id=0x123, is_extended_id=False, data = bytearray([0x12, 0x34, 0x56]), dlc = 4))
        
#         # Important to ensure all outputs are flushed
#         RedirectReader_listener.stop()

#         ###################################
    
#         # Terminal

#         # sudo ip link add vcan1 up type vcan
#         # candup vcan1

#         # Check Print CAN Messages.
     
#         ###################################

#         time.sleep(1.0)


# if __name__ == "__main__":
#     main()

#################################################################


# #!/usr/bin/env python

# import time
# import can

# def main():
#     with can.Bus(receive_own_messages=True) as bus:


#         # BufferedReader Test

#         BufferedReader_listener = can.BufferedReader()
#         msg = bus.recv()

#         # now either call
#         BufferedReader_listener(msg)
#         # or
#         BufferedReader_listener.on_message_received(msg)

#         print(BufferedReader_listener.get_message())
#         print(BufferedReader_listener.get_message())
#         print(BufferedReader_listener.get_message())

#         BufferedReader_listener(can.Message(arbitration_id=0x321, is_extended_id=False, data = bytearray([0x01, 0x02, 0x03]), dlc = 8))
#         print(BufferedReader_listener.get_message())
#         print(BufferedReader_listener.get_message())
#         print(BufferedReader_listener.on_message_received(can.Message(arbitration_id=0x123, is_extended_id=False, data = bytearray([0x12, 0x34, 0x56]), dlc = 4)))
#         print(BufferedReader_listener.get_message())
#         print(BufferedReader_listener.get_message())

#         # Important to ensure all outputs are flushed
#         BufferedReader_listener.stop()
        
    

#         time.sleep(1.0)


# if __name__ == "__main__":
#     main()

###############################################################

#!/usr/bin/env python

import time
import can
import asyncio

async def msg_printer(listener,msg) :
    print(await listener.get_message())
    print(await listener.get_message())
    
    for i in range(10) :
        listener.on_message_received(msg)
        print(await listener.get_message())
        
    # await listener.get_message()

def main():
    with can.Bus(receive_own_messages=True) as bus:

        listener = can.AsyncBufferedReader()
        msg = bus.recv()

        # now either call
        listener(msg)
        # or
        listener.on_message_received(msg)
        asyncio.run(msg_printer(listener,msg))
        print(listener.get_message())


        # Important to ensure all outputs are flushed
        listener.stop()


if __name__ == "__main__":
    main()