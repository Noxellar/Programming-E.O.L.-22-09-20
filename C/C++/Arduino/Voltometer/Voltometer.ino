int voltage;
int pin = 5;

void setup() {
  pinMode(pin, OUTPUT);
  pinMode(GND, INPUT);
  Serial.setup(9600);
}

void loop() {
  line = digitalRead(GND);
  Serial.printl(line);
}
