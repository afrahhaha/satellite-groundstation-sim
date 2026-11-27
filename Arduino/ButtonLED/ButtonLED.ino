// Button-controlled LED: the LED is on while the button is held.
// Wiring: push button between pin 2 and GND (internal pull-up), LED on pin 13.

const int BUTTON_PIN = 2;
const int LED_PIN = 13;

void setup()
{
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
}

void loop()
{
  // active low: the pin reads LOW while the button is pressed
  digitalWrite(LED_PIN, digitalRead(BUTTON_PIN) == LOW ? HIGH : LOW);
}
