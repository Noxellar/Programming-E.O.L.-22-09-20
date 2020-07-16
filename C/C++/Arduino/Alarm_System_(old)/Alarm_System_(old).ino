/* Global Alarm variables */
const int default_pitch = 150;
int pitch = default_pitch;
int offset = 5;

/* Output Pins */
const int buzzer = 6;
const int pin = 5;

void setup() {
  pinMode(pin, INPUT_PULLUP);
}

void loop() {
  if (digitalRead(pin) != LOW) {
    tone(buzzer, pitch);
    pitch += offset;
    
    if (pitch <= default_pitch || pitch >= 800) {
      offset = -offset;
    }
    
    delay(15);
  } else{
    noTone(buzzer);
    offset = 5;
    pitch = default_pitch;
  }
}
