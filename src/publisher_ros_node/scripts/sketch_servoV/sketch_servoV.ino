#include <Servo.h>
unsigned long myTime1;
unsigned long myTime2;

Servo myservob;
Servo myservon;
int intbval;
int intnval;
String intch;

void setup() 
{ 
myservon.attach(9);
Serial.begin(115200);
myservon.write(90);
myservob.attach(10);
myservob.write(90);
//Serial.println("Ready to rotate");
}

String getValue(String data, char separator, int index)
{
    int found = 0;
    int strIndex[] = { 0, -1 };
    int maxIndex = data.length() - 1;

    for (int i = 0; i <= maxIndex && found <= index; i++) {
        if (data.charAt(i) == separator || i == maxIndex) {
            found++;
            strIndex[0] = strIndex[1] + 1;
            strIndex[1] = (i == maxIndex) ? i+1 : i;
        }
    }
    return found > index ? data.substring(strIndex[0], strIndex[1]) : "";
}

void loop() 
{
  if (Serial.available() > 0)
  {
    //intch = Serial.read();
    //Serial.println("received =" + intch);
    intch = Serial.readString();
    intch.toLowerCase();
    if(intch.charAt(0) == 'n')
    {
      intch.replace("n", "");
      intch.trim();
      intnval = intch.toInt();
      //Serial.println("Angular possition n =" + intch);
      myservon.write(intnval);
      delay (1000);
    }
    else if(intch.charAt(0) == 'b')
    {
      //myTime1 = millis();
      Serial.println(myTime1);
      intch.replace("b", "");
      intch.trim();
      intbval = intch.toInt();
      //Serial.println("Angular possition b =" + intch);
      myservob.write(intbval);
      //delay (10);
      //myTime2 = millis();
      //Serial.println(myTime2);
      //Serial.print("Duration b = ");
      //Serial.println(myTime2-myTime1);
      delay (1000);
    }
    else if(intch.charAt(0) == 'a')
    {
      //myTime1 = millis();
      //===================================================
      intch.replace("a", "");
      intch.trim();
      String bval = getValue(intch, ':', 0);
      String nval = getValue(intch, ':', 1);
      //Serial.println("Angular possition base =" + bval);
      //Serial.println("Angular possition neck=" + nval);
      //===================================================
      intbval = bval.toInt();
      myservob.write(intbval);
      intnval = nval.toInt();
      myservon.write(intnval);
      //myTime2 = millis();
      //Serial.print("Duration a = ");
      //Serial.println(myTime2-myTime1);
      //delay (1000);
    }
    
   }
}
