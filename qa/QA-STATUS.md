# QA-status för Asterisk core sounds

Kontrollen gjordes 2026-10-26–2026-10-27 mot `asterisk-core-sounds-sv-manifest.json`.

## Verifierat

- Anton och Louise har vardera exakt 569 filer från den aktuella filkartan.
- Varje fil är mono WAV, signed 16-bit PCM, 48 kHz.
- Inga filer är tomma eller trasiga.
- Inga oväntade byte-identiska WAV-filer finns inom respektive röst.
- De tio `silence/*.wav`-filerna är avsiktlig digital tystnad på 1–10 sekunder.
- Manusens 559 talsträngar passerar `svlang skrivregler`, `svlang svengelska` och `l10n-lint` när de läses som en svensk JSON-katalog.
- Gitleaks är ren för de ändrade generator-, gransknings- och manusfilerna.
- Kandidatarkiven och deras SHA-256-sidofiler har verifierats efter byggning.
- Lyssningsgranskningen är slutförd: samtliga 569 ljud för Anton och samtliga 569 ljud för Louise är godkända. Besluten är hashbundna i `approved-baseline-decisions.json`.

## Nästa steg

- Granska installationsrutinen mot den aktuella Asterisk- eller FreePBX-miljön.
- Hantera eventuell uppströmsinskickning som en separat releaseprocess.

De befintliga `*-candidate-1.6.1.tar.gz`-arkiven är granskningskandidater, inte en uppströmsrelease.
