#!/usr/bin/python3
import rclpy
from rclpy.node import Node
import tkinter as tk
import customtkinter
from std_msgs.msg import String

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('gui_pickup_node')
        self.sub_station = self.create_subscription(String, '/station', self.station_callback, 10)
        self.pub_station = self.create_publisher(String,'/station',10) 

        self.root = tk.Tk()
        self.root.title("Pick Up")
        self.root.geometry("400x220")

        self.label = tk.Label(self.root, text="please take out the stuff")
        self.label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        self.button = tk.Button(master=self.root, text="Submit", command=self.submit_callback)
        self.button.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

    def station_callback(self, msg):
        if msg.data == "PL":              # If the robot is now at the Production Line
            # self.get_logger().info('I heard: "%s"' % msg.data)
            self.root.mainloop() 

    def submit_callback(self):    # user กดหยิบของเสร็จแล้ว >> ให้หลินกลับไปที่ home
        self.root.destroy()
        msg = String()
        msg.data = "Home"
        self.pub_station.publish(msg)
        self.get_logger().info('Home')

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()