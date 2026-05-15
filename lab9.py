int LED1pin = 43;
int LED2pin = 44;
int LED3pin = 45;
int LED4pin = 46;

int button1pin = 38;
int button2pin = 39;
int button3pin = 40;
int button4pin = 41;

byte anlikButon1 = LOW;
byte anlikButon2 = LOW;


byte sonDurum = LOW;
byte sonDurum2 = LOW;

byte anlikYanan = HIGH;
byte anlikMod = 1;

void MOD1(){
  

  digitalWrite(LED1pin , HIGH);
  
  digitalWrite(LED2pin , HIGH);
  
  digitalWrite(LED3pin , HIGH);
  
  digitalWrite(LED4pin , HIGH);

  delay(1000);

  digitalWrite(LED1pin , LOW);
  
  digitalWrite(LED2pin , LOW);
  
  digitalWrite(LED3pin , LOW);
  
  digitalWrite(LED4pin , LOW);

  delay(1000);


}

void MOD3(){

  

    digitalWrite(LED1pin , HIGH);
    delay(1000);
    digitalWrite(LED1pin , LOW);

    digitalWrite(LED2pin , HIGH);
    delay(1000);
    digitalWrite(LED2pin , LOW);

    digitalWrite(LED3pin , HIGH);
    delay(1000);
    digitalWrite(LED3pin , LOW);

    digitalWrite(LED4pin , HIGH);
    delay(1000);
    digitalWrite(LED4pin , LOW);
  

}
void MOD2(){

    digitalWrite(LED4pin , HIGH);
    delay(1000);
    digitalWrite(LED4pin , LOW);

    digitalWrite(LED3pin , HIGH);
    delay(1000);
    digitalWrite(LED3pin , LOW);

    digitalWrite(LED2pin , HIGH);
    delay(1000);
    digitalWrite(LED2pin , LOW);

    digitalWrite(LED1pin , HIGH);
    delay(1000);
    digitalWrite(LED1pin , LOW);
  
}


void setup() {
pinMode(LED1pin, OUTPUT);
pinMode(LED2pin, OUTPUT);
pinMode(LED3pin, OUTPUT);
pinMode(LED4pin, OUTPUT);
pinMode(button1pin, INPUT);
pinMode(button2pin, INPUT);
}



void loop() {
  anlikButon1 = digitalRead(button1pin);
  anlikButon2 = digitalRead(button2pin);

  if(anlikButon1 == HIGH){
    if(sonDurum == LOW){
      digitalWrite(LED1pin , HIGH);
      digitalWrite(LED2pin , HIGH);
      digitalWrite(LED3pin , HIGH);
      digitalWrite(LED4pin , HIGH);
      sonDurum = HIGH;
    }
    else{
      digitalWrite(LED1pin , LOW);
      digitalWrite(LED2pin , LOW);
      digitalWrite(LED3pin , LOW);
      digitalWrite(LED4pin , LOW);
      sonDurum = LOW;
    }
  }

  if(anlikButon2 == HIGH){

    if(anlikMod == 1){
      MOD1();
      anlikMod = 2;
    }
    else if(anlikMod == 2){
      MOD2();
      anlikMod = 3;
    }
    else if(anlikMod == 3){
      MOD3();
      anlikMod = 1;
    }  
  }




 
}