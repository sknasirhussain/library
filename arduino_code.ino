#include <SPI.h>
#include <MFRC522.h>

constexpr uint8_t RST_PIN = D3;
constexpr uint8_t SS_PIN = D4;

MFRC522 rfid(SS_PIN, RST_PIN); // Instance of the class
MFRC522::MIFARE_Key key;

String studentTag = "";
String bookTag = "";

void setup() {
  Serial.begin(9600);
  SPI.begin();
  rfid.PCD_Init();
  pinMode(D8, OUTPUT);
}

void loop() {
  if (rfid.PICC_IsNewCardPresent() && rfid.PICC_ReadCardSerial()) {
    if (studentTag == "") {
      // Read Student Tag
      for (byte i = 0; i < 4; i++) {
        studentTag += rfid.uid.uidByte[i];
      }
      Serial.print("Student: ");
      Serial.println(studentTag);
      rfid.PICC_HaltA();
      rfid.PCD_StopCrypto1();
    } else if (bookTag == "") {
      // Read Book Tag
      for (byte i = 0; i < 4; i++) {
        bookTag += rfid.uid.uidByte[i];
      }
      Serial.print("Book: ");
      Serial.println(bookTag);
      rfid.PICC_HaltA();
      rfid.PCD_StopCrypto1();
    }
    // Reset tags after both are read
    if (studentTag != "" && bookTag != "") {
      studentTag = "";
      bookTag = "";
    }
  }
}
