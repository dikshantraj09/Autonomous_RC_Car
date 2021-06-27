#include <Servo.h> 
#include <ros.h>
#include <std_msgs/UInt16.h>
#include <sensor_msgs/Joy.h> 
#include <std_msgs/Float32.h>
#include <geometry_msgs/Twist.h>
ros::NodeHandle  nh;
 
// Motor A connections
int enA = 9;
int in1 = 8;
int in2 = 7;
int enB = 4;
int in3 = 6;
int in4 = 5;
Servo servo;

void messageCb( const geometry_msgs::Twist& msg)
{ int angle=msg.angular.x;
  int mspeed=msg.linear.x;
  if (mspeed<0){
  //Serial.print(mspeed);
      digitalWrite(in2, HIGH);
      digitalWrite(in1, LOW);
      digitalWrite(in4, LOW);
      digitalWrite(in3, HIGH);
      analogWrite(enA,-mspeed);
      analogWrite(enB,-mspeed);
  }
  else{
      digitalWrite(in1, HIGH);
      digitalWrite(in2, LOW);
      digitalWrite(in3, LOW);
      digitalWrite(in4, HIGH);
      analogWrite(enB,mspeed);
      analogWrite(enA,mspeed);
  }
  if(angle==90){
  servo.write(90);  
}
  else{
  servo.write(angle);
}


}

ros::Subscriber<geometry_msgs::Twist> sub("cmd_vel", &messageCb );

void setup(){
  nh.initNode();
  nh.subscribe(sub);
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  digitalWrite(enA, HIGH);
  digitalWrite(enB, HIGH);
  //analogWrite(enA,200);
  servo.attach(3); //attach it to pin 9
  
}

void loop(){
  nh.spinOnce();
  delay(1);
}
