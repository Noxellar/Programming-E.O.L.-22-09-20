/*
   Alarm System for protection of FTTB (Fluffy The Teddy Bear)
   Modules:
    Arduino Uno
    Thinkershield
   Code by Harry Le
   Box and design by Pranith Reddy
*/

#define null 0

/* Global Alarm variables */
const int default_pitch = 150;
int pitch = default_pitch;
int offset = 5;

/* Output Pins */
const int LED = 4;
const int triggerPin = 6;
const int echoPin = 2;
const int buzzer = A3;
const int circuitPin = A0;

/* Ultrasonic Depth Sensors variables */
float prev_len = null;
float pres_len = 0;
float duration;

void setup() {
  pinMode(triggerPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(circuitPin, INPUT_PULLUP);
  pinMode(LED, OUTPUT);
  // Setup for Serial monitor
  Serial.begin(9600);
}

void loop() {
  // Set LED to LOW
  digitalWrite(LED, LOW);

  // Call the function ultrasonics
  ultrasonics();

  // Turn on circuitPin
  digitalWrite(circuitPin, HIGH);

  /*
    See to it that at the start that the difference
      between prev_len and pres_len on the first go isn't
      bigger than 0.75
  */

  if (prev_len == null) {
    prev_len = pres_len;
  }

  /*
    See if the circuit is broken or that the distance
      between the bottom of the box and the lid of the box
      hasn't changed drasatically (more than 2 centimetres)
  */
  if (digitalRead(circuitPin) != LOW || abs(pres_len - prev_len) > 2) {
    // Turn on LED
    digitalWrite(LED, HIGH);

    Serial.println();
    // Sound the alarm forever until manually disabled
    while (true) {
      tone(buzzer, pitch);
      pitch += offset;

      if (pitch <= default_pitch || pitch >= 850) {
        offset = -offset;
      }

      delay(15);
    }
  } else {
    // Turn off circuitPin
    digitalWrite(circuitPin, LOW);
  }

  /*
    Wait a random amount of time
    This way, the robber can't move slowly
    as the distance of the Ultrasonic Depth
    Sensor always changes by a few micrometres
  */
  delay((rand() % 5) * 500);
}

void ultrasonics() {
  // Turn off triggerPin
  digitalWrite(triggerPin, LOW);
  // Wait 2 microsecond (0.002 milliseconds)
  delayMicroseconds(2);
  // Turn on triggerPin
  digitalWrite(triggerPin, HIGH);
  // Wait 10 microseconds (0.01 milliseconds)
  delayMicroseconds(10);
  // Turn off triggerPin
  digitalWrite(triggerPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  // Set new values for prev_len and pres_len
  prev_len = pres_len;
  pres_len = microsecondsToCentimeters(duration);
  // Print present length to Serial monitor
  Serial.print(pres_len);
  Serial.println();
}

float microsecondsToCentimeters(float microseconds) {
  // Apparently there are 29 microseconds in a centimetre
  // Divide by 2 since pings cover to and from
  return microseconds / 29 / 2;
}
