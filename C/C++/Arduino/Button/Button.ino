const int buttonPin = 7;
const int pin = 6;

int buzzer = 5;
const int default_pitch = 150;
int pitch  = default_pitch;
int offset = 5;

int buttonState = 0;

void setup() {
  pinMode(pin, OUTPUT);
  pinMode(buttonPin, INPUT);
}

void loop() {
  buttonState = digitalRead(buttonPin);

  if (buttonState == HIGH) {
    tone(buzzer, pitch);
    pitch += offset;
    
    if (pitch <= default_pitch || pitch >= 800) {
      offset = -offset;
    }
    
    delay(15);
  } else {
    noTone(buzzer);
    pitch = default_pitch;
  }
}
