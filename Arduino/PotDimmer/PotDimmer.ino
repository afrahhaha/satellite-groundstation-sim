// Potentiometer LED dimmer (Task 4).
// The pot position sets the LED brightness through PWM.
// Wiring: potentiometer wiper on A0, LED (with resistor) on pin 9.
// Note: the LED must be on a PWM pin (3, 5, 6, 9, 10 or 11 on an Uno).
// Pin 13 has no PWM, so analogWrite() there only switches the LED fully on/off.

const int POT_PIN = A0;
const int LED_PIN = 9;

void setup()
{
  pinMode(LED_PIN, OUTPUT);
}

void loop()
{
  int reading = analogRead(POT_PIN);                 // 0..1023
  int brightness = map(reading, 0, 1023, 0, 255);    // 0..255 PWM duty
  analogWrite(LED_PIN, brightness);
}
