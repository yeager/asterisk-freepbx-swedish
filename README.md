# Svenska Asterisk- och FreePBX-ljud

Kompletta svenska core-sound-paket för Asterisk och FreePBX, med rösterna Anton och Louise.

Det ursprungliga svenska paketet Asterisk-prompt-se skapades av Daniel Nylander 2006. Den här utgåvan innehåller nya inspelningar med Anton och Louise.

## Innehåll

Varje paket innehåller Asterisk 1.6.1:s fullständiga filkarta med 569 resurser:

- 552 talfiler
- 10 avsiktliga tystnadsfiler
- 7 funktionella toner och signaler

Alla WAV-filer är mono, 48 kHz, 16-bitars signed PCM. Varje ljud har lyssningsgranskats och godkänts. Filkartan och de hashbundna granskningsbesluten finns i repot.

## Asterisk-prompt-se från 2006

Det äldre paketet `asterisk-prompt-se` 1.045 innehåller fler än bara Asterisks senare core-sound-filuppsättning. Jämförelsen mot Anton visar 393 gemensamma filnamn, 1 027 äldre filnamn som saknas i Anton och 176 nyare Anton-filer som inte fanns i 2006-paketet. De saknade filerna omfattar bland annat 267 svenska riktnummer, 99 hemautomationsprompter, 30 väderprompter och 579 äldre rotprompter.

Den kompletta maskinläsbara jämförelsen finns i [compat/asterisk-prompt-se-1.045-gap.json](compat/asterisk-prompt-se-1.045-gap.json). Skapa den igen med `scripts/compare_legacy_prompt_se.py` och en extraherad kopia av originalpaketets `sounds/`-katalog.

## Hämta och installera

Hämta den önskade rösten från den senaste [releasen](https://github.com/yeager/asterisk-freepbx-swedish/releases/latest), kontrollera SHA-256-filen och packa upp arkivet i Asterisks svenska ljudkatalog:

```sh
shasum -a 256 -c asterisk-core-sounds-sv-anton-1.6.1.tar.gz.sha256
sudo tar -xzf asterisk-core-sounds-sv-anton-1.6.1.tar.gz -C /var/lib/asterisk/sounds/sv
```

Ställ sedan in språket `sv` i dialplanen eller i FreePBX. Sökvägen kan skilja sig mellan installationer; kontrollera Asterisks konfiguration före extrahering.

## Paket och kontroll

Releaserna innehåller ett ljudarkiv och en SHA-256-sidofil per röst. Arkiven innehåller endast den fullständiga WAV-filstrukturen som Asterisk använder. `core-sounds-sv.txt`, `CREDITS` och `LICENSE` finns i repot för dokumentation och en eventuell Asterisk-inskickning.

Kör följande för att kontrollera ett källpaket eller bygga ett nytt arkiv från en katalog med WAV-filer:

```sh
python3 scripts/package_release.py --voice anton --source /sökväg/till/anton --output dist
```

Skriptet kräver exakt filkarta, kontrollerar mono PCM16/48 kHz och skapar både arkiv och SHA-256-sidofil.

## Licens och krediter

Ljud och medföljande material publiceras under [CC BY-SA 3.0](LICENSE). Se [CREDITS](CREDITS) för paketets krediter.

## Uppströmsbidrag

Paketet är förberett för en Asterisk-inskickning. Se [docs/UPSTREAM-SUBMISSION.md](docs/UPSTREAM-SUBMISSION.md) för de extra krav som Asterisk ställer innan en inskickning kan göras.
