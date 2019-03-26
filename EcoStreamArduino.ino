#include <Servo.h>

Servo flapControlMetal;
Servo flapControlOrg;
Servo flapControlGlass;
Servo flapControlPlastic;
int mot1=5;
int mot2=9;
int indProxPin = 10;
int conveyorPins[2] = {3,4};

void runConveyor(void);
void haltConveyor(void);
void kickerMetal (void);
void kickerOrg (void);
void kickerGlass (void);
void kickerPlastic (void);
bool checkMetal (int);
void lvlZero (void);
void lvlOne (void);

void setup()
{
 //Initialize all of the variables
 pinMode(mot1,OUTPUT);
 pinMode(mot2,OUTPUT);
 pinMode(indProxPin, INPUT);
 flapControlMetal.attach(11);
 flapControlOrg.attach(12);
 flapControlGlass.attach(13);
 flapControlPlastic.attach(14);
}

void loop() 
{
  //These functions run the different levels 
  lvlZero();
  lvlOne();
}

void conveyorRun (void)
{
    //Runs the Conveyor Belt Forward
    for (int i = 0; i < 2; i++)
    {
      analogWrite(mot1, 255);
      analogWrite(mot2, 255);
    }
    /*
    delay(750);
    for (int i = 0; i < conveyorPins.length; i++)
    {
      analogWrite(mot1, 0);
      analogWrite(mot2, 0);
    }
    delay(250);
    */ 
}
//Runs the full code for the First Level
void lvlOne (void)
{
  while(1)
  {
    runConveyor();
    delay(250);
    haltConveyor();
    if (checkMetal(indProxPin))
    {
      kickerMetal();
    }
    if (checkCapacitator == attr.plastic)
    {
      kickerPlastic();  
    }
    if (checkCapacitator == attr.metal)
    {
      kickerMetal();
    }
    
    if (checkCapacitator == attr.org)
    {
      kickerOrg();
    }
    
    if (checkCapacitator == attr.glass)
    {
      kickerGlass();
    }
    
    
    if (mot1 && mot2 == 360){
      break;  
    }
  }
}
//Full code for the Second Level of the machine
void lvlTwo (void)
{
  while(1)
  {
    runConveyor();
    delay(250);
    haltConveyor();
    if (checkMetal(indProxPin))
    {
      kickerMetal();
    }
    if (mot1 && mot2 == 360){
      break;  
    }
}

//Runs Induction Proximity sensor and returns whether there is metal or not
bool checkMetal(int indProxPin)
{
    sensorState = digitalRead(indProxPin);
    if (sensorState == LOW):
        return false;
    else if (sensorState == HIGH):
        return true;
    else:
        return null;
}


//Activates the "kick" sequence. Opens flap and sorts the trash into component.

void kickerMetal (void)
{
  flapControlMetal.write(90);
  delay(250);
  flapControlMetal.write(0);
}
void kickerOrg (void)
{
  flapControlOrg.write(90);
  delay(250);
  flapControlOrg.write(0);
}
void kickerPlastic (void)
{
  flapControlPlastic.write(90);
  delay(250);
  flapControlPlastic.write(0);
}
void kickerGlass (void)
{
  flapControlGlass.write(90);
  delay(250);
  flapControlGlass.write(0);
}

void haltConveyor (void)
{
  //Stops Conveyor
  analogWrite(mot1, 0)
  analogWrite(mot2, 0)
}
