int pin2 = 2;
int pin4 = 4;

void setup() {
  pinMode(pin2, OUTPUT);
  pinMode(pin4, OUTPUT);
}

void loop() {
  digitalWrite(pin4, HIGH);
  digitalWrite(pin2, LOW);
  delay(1000);
  digitalWrite(pin4, LOW);
  digitalWrite(pin2, HIGH);
  delay(1000);
}
