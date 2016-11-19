#include <DigiUSB.h>
int sensorValue = 0;
int a = 0;

void setup() {
	DigiUSB.begin();
	pinMode(1, OUTPUT); //LED on Model B
	pinMode(0, INPUT);
	DigiUSB.refresh();
}

void loop() {
	sensorValue = digitalRead(0);
	if (sensorValue == HIGH) {
		a = 0;
		digitalWrite(1, HIGH);
		DigiUSB.write("1");
		DigiUSB.refresh();
		while (a<30000) {
			a = a + 1;
		}
	}
	else {
		digitalWrite(1, LOW);
		DigiUSB.write("0");
		DigiUSB.refresh();
		while (a<30000) {
			a = a + 1;
		}


	}

}