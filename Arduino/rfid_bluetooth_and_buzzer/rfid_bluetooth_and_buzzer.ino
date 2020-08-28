#include <SoftwareSerial.h>
#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN         9           // Configurable, see typical pin layout above
#define SS_PIN          10          // Configurable, see typical pin layout above
const int rxpin = 7;  
const int txpin = 6;
String Uids;
String Nameic;
const int buzzer = 4; //buzzer to arduino pin 9
String FullDatum;

MFRC522 mfrc522(SS_PIN, RST_PIN);   // Create MFRC522 instance
SoftwareSerial bluetooth(rxpin, txpin);

//*****************************************************************************************//
void setup() {
  Serial.begin(9600);                                           // Initialize serial communications with the PC
  SPI.begin();                                                  // Init SPI bus
  mfrc522.PCD_Init();                                              // Init MFRC522 card
  bluetooth.begin(9600);
  pinMode(buzzer, OUTPUT); // Set buzzer - pin 9 as an output 
  
  
}

//*****************************************************************************************//
void loop() {

  // Prepare key - all keys are set to FFFFFFFFFFFFh at chip delivery from the factory.
  MFRC522::MIFARE_Key key;
  for (byte i = 0; i < 6; i++) key.keyByte[i] = 0xFF;

  //some variables we need
  byte block;
  byte len;
  Uids = "";
  Nameic = "";
  FullDatum = "";

  MFRC522::StatusCode status;

  //-------------------------------------------

  // Reset the loop if no new card present on the sensor/reader. This saves the entire process when idle.
  if ( ! mfrc522.PICC_IsNewCardPresent()) {
    return;
  }

  // Select one of the cards
  if ( ! mfrc522.PICC_ReadCardSerial()) {
    return;
  }

  //-------------------------------------------
  //Serial.println( mfrc522.uid.uidByte[0]- '0'+ mfrc522.uid.uidByte[1]- '0'+mfrc522.uid.uidByte[2]- '0'+mfrc522.uid.uidByte[3]- '0');
    Uids = String (mfrc522.uid.uidByte[0]- '0')+ 
      String (mfrc522.uid.uidByte[1]- '0')+
      String (mfrc522.uid.uidByte[2]- '0')+
      String (mfrc522.uid.uidByte[3]- '0');

  //mfrc522.PICC_DumpDetailsToSerial(&(mfrc522.uid)); //dump some details about the card

  //mfrc522.PICC_DumpToSerial(&(mfrc522.uid));      //uncomment this to see all blocks in hex

  //-------------------------------------------
  byte buffer1[18];

  block = 4;
  len = 18;
  //---------------------------------------- GET LAST NAME

  byte buffer2[18];
  block = 1;

  status = mfrc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, 1, &key, &(mfrc522.uid)); //line 834
  if (status != MFRC522::STATUS_OK) {
    return;
  }

  status = mfrc522.MIFARE_Read(block, buffer2, &len);
  if (status != MFRC522::STATUS_OK) {
    return;
  }

  //PRINT LAST NAME
  for (uint8_t i = 0; i < 14; i++) {
    Nameic = Nameic + char(buffer2[i]);  
   
  }
  
  Nameic.trim();
  
  FullDatum = Nameic+"_"+Uids+"_"+ "1"+"\n" ;
  Serial.println(FullDatum);
  Serial.println("");
  bluetooth.print(FullDatum);
  tone(buzzer, 1500); // Send 1KHz sound signal...
  delay(105);        // ...for 1 sec
  noTone(buzzer);     // Stop sound...

  
    

  //----------------------------------------

  delay(10); //change value if you want to read cards faster

  mfrc522.PICC_HaltA();
  mfrc522.PCD_StopCrypto1();
}
//*****************************************************************************************//
