// 4-bit binary counter (Task 3).
// Each button press adds 1 to a count from 0 to 15, shown in binary on 4 LEDs.
// Wiring: push button between pin 2 and GND (internal pull-up),
//         LEDs on pins 8 (bit 0, LSB) to 11 (bit 3, MSB).

const int BUTTON_PIN = 2;
const int LED_PINS[4] = {8, 9, 10, 11};
const unsigned long DEBOUNCE_MS = 50;

int count = 0;
int stableState = HIGH;          // debounced button state
int lastReading = HIGH;          // raw reading from the previous loop
unsigned long lastChangeTime = 0;

void showCount(int value)
{
  for (int bit = 0; bit < 4; bit++) {
    digitalWrite(LED_PINS[bit], (value >> bit) & 1 ? HIGH : LOW);
  }
}

void setup()
{
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  for (int bit = 0; bit < 4; bit++) {
    pinMode(LED_PINS[bit], OUTPUT);
  }
  showCount(count);
}

void loop()
{
  int reading = digitalRead(BUTTON_PIN);

  // restart the debounce timer whenever the raw reading changes
  if (reading != lastReading) {
    lastChangeTime = millis();
    lastReading = reading;
  }

  // accept the new state only once it has been steady for DEBOUNCE_MS
  if (millis() - lastChangeTime > DEBOUNCE_MS && reading != stableState) {
    stableState = reading;
    if (stableState == LOW) {          // count on press
      count = (count + 1) % 16;        // wrap 15 -> 0
      showCount(count);
    }
  }
}
