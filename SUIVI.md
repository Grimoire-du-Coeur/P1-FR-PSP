# Avancement de la traduction

> Fichier **généré**. Ne pas le modifier à la main : chaque fusion l'écrase.

```text
Relecture      █░░░░░░░░░░░░░░░░░░░░░░░    4 %       10 / 284 scripts relus
Dialogues      ████████████████████████  100 %    8 560 / 8 572 textes
EBOOT          ████████████████████████  100 %    2 956 / 2 956 textes
Donjons        ████████████████████████  100 %      130 / 130 textes
Négociations   ████████████████████████  100 %   12 487 / 12 487 textes
Noms           ████████████████████████  100 %      439 / 439 textes

Total          ████████████████████████  100 %   24 572 / 24 584 textes
```

La **relecture** se compte en scripts, pas en textes : on relit un fichier d'un bout à l'autre ou pas du tout. Un script compte pour relu quand son issue `Relecture : …` est **fermée**, c'est-à-dire quand ses retours ont été traités. Le plus simple pour relire est [l'outil de relecture](https://codebyhaamza.github.io/p1-relecture/) : rien à installer, il montre ce qui est déjà pris et mène au prochain script que personne n'a lu.

## Poids à surveiller

Ces entrées alourdissent leur fichier. Un bloc qui franchit sa frontière fait rester **tout le fichier en anglais** dans le jeu, sans erreur au build : c'est le plus sournois des avertissements.

- [`E0_024.json`](trad/dialogues/E0_024.json) — 3 entrées
- [`BASKET_006.json`](trad/negociations/BASKET_006.json) — 1 entrée
- [`BASKET_007.json`](trad/negociations/BASKET_007.json) — 1 entrée
- [`KOROU_002.json`](trad/negociations/KOROU_002.json) — 1 entrée
- [`KOUMAN_001.json`](trad/negociations/KOUMAN_001.json) — 2 entrées
- [`SINSI_003.json`](trad/negociations/SINSI_003.json) — 2 entrées
- [`SYOUJO_001.json`](trad/negociations/SYOUJO_001.json) — 1 entrée
- [`SYOUJO_002.json`](trad/negociations/SYOUJO_002.json) — 1 entrée
- [`SYOUJO_003.json`](trad/negociations/SYOUJO_003.json) — 1 entrée
- [`SYOUJO_005.json`](trad/negociations/SYOUJO_005.json) — 4 entrées
- [`SYOUJO_006.json`](trad/negociations/SYOUJO_006.json) — 4 entrées
- [`TOILET_001.json`](trad/negociations/TOILET_001.json) — 1 entrée

## À relire

Terminologie à confirmer — un terme du dictionnaire apparaît dans l'anglais sans sa traduction officielle dans le français. Ce n'est pas forcément une faute, mais ça mérite un avis.

- [`E0_043.json`](trad/dialogues/E0_043.json) — 1 terme

## Largeur à surveiller

Ces lignes sont plus larges que l'anglaise et approchent de la limite de la boîte. Elles ne débordent pas à coup sûr, mais un `{SAUT}` de plus serait plus sage.

- [`E1_003.json`](trad/dialogues/E1_003.json) — 1 ligne
- [`E1_012.json`](trad/dialogues/E1_012.json) — 1 ligne
- [`E1_016.json`](trad/dialogues/E1_016.json) — 1 ligne
- [`E1_023.json`](trad/dialogues/E1_023.json) — 1 ligne
- [`E1_026.json`](trad/dialogues/E1_026.json) — 1 ligne
- [`E2_001.json`](trad/dialogues/E2_001.json) — 1 ligne
- [`E3_007.json`](trad/dialogues/E3_007.json) — 1 ligne
- [`DNG_001.json`](trad/donjons/DNG_001.json) — 2 lignes
- [`KEMONO_007.json`](trad/negociations/KEMONO_007.json) — 1 ligne
- [`KOKURI_001.json`](trad/negociations/KOKURI_001.json) — 1 ligne
- [`SYOUJO_001.json`](trad/negociations/SYOUJO_001.json) — 1 ligne
- [`TOILET_001.json`](trad/negociations/TOILET_001.json) — 2 lignes
- [`ARMES_001.json`](trad/noms/ARMES_001.json) — 1 ligne
- [`OBJETS_002.json`](trad/noms/OBJETS_002.json) — 1 ligne

## À vérifier en jeu

Ces lignes dépassent la place que l'anglais occupe dans l'exécutable. Le moteur les redirige vers un espace libre et ça marche — « Charger une partie » le fait déjà — mais c'est plus fragile que de tenir dans le budget. Un coup d'œil à l'écran suffit à confirmer.

- [`EBOOT_001.json`](trad/eboot/EBOOT_001.json) — 5 lignes
- [`EBOOT_002.json`](trad/eboot/EBOOT_002.json) — 2 lignes
- [`EBOOT_003.json`](trad/eboot/EBOOT_003.json) — 15 lignes
- [`EBOOT_004.json`](trad/eboot/EBOOT_004.json) — 1 ligne
- [`EBOOT_010.json`](trad/eboot/EBOOT_010.json) — 10 lignes
- [`EBOOT_011.json`](trad/eboot/EBOOT_011.json) — 5 lignes
- [`EBOOT_012.json`](trad/eboot/EBOOT_012.json) — 15 lignes
- [`EBOOT_013.json`](trad/eboot/EBOOT_013.json) — 5 lignes
- [`EBOOT_014.json`](trad/eboot/EBOOT_014.json) — 20 lignes
- [`EBOOT_015.json`](trad/eboot/EBOOT_015.json) — 21 lignes
- [`EBOOT_016.json`](trad/eboot/EBOOT_016.json) — 7 lignes
- [`EBOOT_017.json`](trad/eboot/EBOOT_017.json) — 1 ligne
- [`EBOOT_018.json`](trad/eboot/EBOOT_018.json) — 16 lignes
- [`EBOOT_019.json`](trad/eboot/EBOOT_019.json) — 8 lignes
- [`EBOOT_020.json`](trad/eboot/EBOOT_020.json) — 3 lignes
- [`EBOOT_021.json`](trad/eboot/EBOOT_021.json) — 25 lignes
- [`EBOOT_022.json`](trad/eboot/EBOOT_022.json) — 2 lignes
- [`EBOOT_023.json`](trad/eboot/EBOOT_023.json) — 4 lignes
- [`EBOOT_024.json`](trad/eboot/EBOOT_024.json) — 1 ligne
- [`EBOOT_025.json`](trad/eboot/EBOOT_025.json) — 10 lignes
- [`EBOOT_026.json`](trad/eboot/EBOOT_026.json) — 23 lignes
- [`EBOOT_027.json`](trad/eboot/EBOOT_027.json) — 16 lignes
- [`EBOOT_028.json`](trad/eboot/EBOOT_028.json) — 17 lignes
- [`EBOOT_029.json`](trad/eboot/EBOOT_029.json) — 22 lignes
- [`EBOOT_030.json`](trad/eboot/EBOOT_030.json) — 29 lignes
- [`EBOOT_031.json`](trad/eboot/EBOOT_031.json) — 5 lignes
- [`EBOOT_032.json`](trad/eboot/EBOOT_032.json) — 2 lignes

## Dialogues

Prends un fichier **libre**, dis-le en ouvrant ta proposition, et il passera en « en cours » dans la minute.

| Fichier | Textes | Traduits | % | État |
|---|---:|---:|---:|---|
| [`E0_001.json`](trad/dialogues/E0_001.json) | 99 | 99 | 100 % | terminé par @CodeByHaamza · relu (#127) |
| [`E0_002.json`](trad/dialogues/E0_002.json) | 92 | 92 | 100 % | terminé par @CodeByHaamza |
| [`E0_003.json`](trad/dialogues/E0_003.json) | 40 | 40 | 100 % | terminé par @CodeByHaamza |
| [`E0_004.json`](trad/dialogues/E0_004.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`E0_005.json`](trad/dialogues/E0_005.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`E0_006.json`](trad/dialogues/E0_006.json) | 18 | 18 | 100 % | terminé |
| [`E0_007.json`](trad/dialogues/E0_007.json) | 97 | 97 | 100 % | terminé par @CodeByHaamza |
| [`E0_008.json`](trad/dialogues/E0_008.json) | 93 | 93 | 100 % | terminé par @CodeByHaamza |
| [`E0_009.json`](trad/dialogues/E0_009.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`E0_010.json`](trad/dialogues/E0_010.json) | 86 | 86 | 100 % | terminé par @CodeByHaamza |
| [`E0_011.json`](trad/dialogues/E0_011.json) | 67 | 67 | 100 % | terminé par @CodeByHaamza |
| [`E0_012.json`](trad/dialogues/E0_012.json) | 55 | 55 | 100 % | terminé par @CodeByHaamza |
| [`E0_013.json`](trad/dialogues/E0_013.json) | 85 | 85 | 100 % | terminé par @CodeByHaamza |
| [`E0_014.json`](trad/dialogues/E0_014.json) | 91 | 91 | 100 % | terminé par @CodeByHaamza |
| [`E0_015.json`](trad/dialogues/E0_015.json) | 66 | 66 | 100 % | terminé par @CodeByHaamza |
| [`E0_016.json`](trad/dialogues/E0_016.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`E0_017.json`](trad/dialogues/E0_017.json) | 56 | 56 | 100 % | terminé par @CodeByHaamza |
| [`E0_018.json`](trad/dialogues/E0_018.json) | 83 | 83 | 100 % | terminé par @CodeByHaamza |
| [`E0_019.json`](trad/dialogues/E0_019.json) | 58 | 58 | 100 % | terminé par @CodeByHaamza |
| [`E0_020.json`](trad/dialogues/E0_020.json) | 87 | 87 | 100 % | terminé par @CodeByHaamza |
| [`E0_021.json`](trad/dialogues/E0_021.json) | 89 | 89 | 100 % | terminé par @CodeByHaamza |
| [`E0_022.json`](trad/dialogues/E0_022.json) | 52 | 52 | 100 % | terminé par @CodeByHaamza |
| [`E0_023.json`](trad/dialogues/E0_023.json) | 65 | 65 | 100 % | terminé par @CodeByHaamza |
| [`E0_024.json`](trad/dialogues/E0_024.json) | 96 | 96 | 100 % | terminé par @CodeByHaamza · 3 à alléger |
| [`E0_025.json`](trad/dialogues/E0_025.json) | 93 | 93 | 100 % | terminé par @CodeByHaamza |
| [`E0_026.json`](trad/dialogues/E0_026.json) | 77 | 77 | 100 % | terminé par @CodeByHaamza |
| [`E0_027.json`](trad/dialogues/E0_027.json) | 40 | 40 | 100 % | terminé par @CodeByHaamza |
| [`E0_028.json`](trad/dialogues/E0_028.json) | 78 | 78 | 100 % | terminé par @vikmorp, @CodeByHaamza |
| [`E0_029.json`](trad/dialogues/E0_029.json) | 55 | 55 | 100 % | terminé par @CodeByHaamza |
| [`E0_030.json`](trad/dialogues/E0_030.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`E0_031.json`](trad/dialogues/E0_031.json) | 74 | 74 | 100 % | terminé par @CodeByHaamza |
| [`E0_032.json`](trad/dialogues/E0_032.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`E0_033.json`](trad/dialogues/E0_033.json) | 74 | 74 | 100 % | terminé par @CodeByHaamza |
| [`E0_034.json`](trad/dialogues/E0_034.json) | 70 | 70 | 100 % | terminé par @CodeByHaamza |
| [`E0_035.json`](trad/dialogues/E0_035.json) | 57 | 57 | 100 % | terminé par @DiCEO0, @CodeByHaamza |
| [`E0_036.json`](trad/dialogues/E0_036.json) | 53 | 53 | 100 % | terminé par @CodeByHaamza |
| [`E0_037.json`](trad/dialogues/E0_037.json) | 99 | 99 | 100 % | terminé par @CodeByHaamza |
| [`E0_038.json`](trad/dialogues/E0_038.json) | 79 | 79 | 100 % | terminé par @CodeByHaamza |
| [`E0_039.json`](trad/dialogues/E0_039.json) | 56 | 56 | 100 % | terminé par @CodeByHaamza |
| [`E0_040.json`](trad/dialogues/E0_040.json) | 89 | 89 | 100 % | terminé par @CodeByHaamza |
| [`E0_041.json`](trad/dialogues/E0_041.json) | 89 | 89 | 100 % | terminé par @Colonel-Maskou, @CodeByHaamza |
| [`E0_042.json`](trad/dialogues/E0_042.json) | 82 | 82 | 100 % | terminé par @s3rei, @CodeByHaamza |
| [`E0_043.json`](trad/dialogues/E0_043.json) | 100 | 100 | 100 % | terminé par @Colonel-Maskou, @CodeByHaamza · 1 terme |
| [`E0_044.json`](trad/dialogues/E0_044.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`E0_045.json`](trad/dialogues/E0_045.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`E0_046.json`](trad/dialogues/E0_046.json) | 92 | 92 | 100 % | terminé par @CodeByHaamza |
| [`E0_047.json`](trad/dialogues/E0_047.json) | 69 | 69 | 100 % | terminé par @CodeByHaamza |
| [`E0_048.json`](trad/dialogues/E0_048.json) | 50 | 50 | 100 % | terminé par @Gyotre, @ATMC14, @CodeByHaamza |
| [`E1_001.json`](trad/dialogues/E1_001.json) | 80 | 77 | 96 % | commencé par @CodeByHaamza |
| [`E1_002.json`](trad/dialogues/E1_002.json) | 100 | 99 | 99 % | commencé par @CodeByHaamza |
| [`E1_003.json`](trad/dialogues/E1_003.json) | 94 | 94 | 100 % | terminé par @CodeByHaamza · 1 trop large |
| [`E1_004.json`](trad/dialogues/E1_004.json) | 87 | 87 | 100 % | terminé par @CodeByHaamza |
| [`E1_005.json`](trad/dialogues/E1_005.json) | 81 | 76 | 94 % | commencé par @CodeByHaamza |
| [`E1_006.json`](trad/dialogues/E1_006.json) | 77 | 74 | 96 % | commencé par @CodeByHaamza |
| [`E1_007.json`](trad/dialogues/E1_007.json) | 97 | 97 | 100 % | terminé par @CodeByHaamza |
| [`E1_008.json`](trad/dialogues/E1_008.json) | 74 | 74 | 100 % | terminé par @vikmorp, @CodeByHaamza |
| [`E1_009.json`](trad/dialogues/E1_009.json) | 75 | 75 | 100 % | terminé par @CodeByHaamza |
| [`E1_010.json`](trad/dialogues/E1_010.json) | 63 | 63 | 100 % | terminé par @CodeByHaamza |
| [`E1_011.json`](trad/dialogues/E1_011.json) | 87 | 87 | 100 % | terminé par @CodeByHaamza |
| [`E1_012.json`](trad/dialogues/E1_012.json) | 83 | 83 | 100 % | terminé par @CodeByHaamza · 1 trop large |
| [`E1_013.json`](trad/dialogues/E1_013.json) | 60 | 60 | 100 % | terminé par @Uolil-Raccoon, @CodeByHaamza |
| [`E1_014.json`](trad/dialogues/E1_014.json) | 43 | 43 | 100 % | terminé par @CodeByHaamza |
| [`E1_015.json`](trad/dialogues/E1_015.json) | 65 | 65 | 100 % | terminé par @CodeByHaamza |
| [`E1_016.json`](trad/dialogues/E1_016.json) | 100 | 100 | 100 % | terminé par @Uolil-Raccoon, @CodeByHaamza · 1 trop large |
| [`E1_017.json`](trad/dialogues/E1_017.json) | 38 | 38 | 100 % | terminé par @CodeByHaamza |
| [`E1_018.json`](trad/dialogues/E1_018.json) | 100 | 100 | 100 % | terminé par @Uolil-Raccoon, @CodeByHaamza |
| [`E1_019.json`](trad/dialogues/E1_019.json) | 46 | 46 | 100 % | terminé par @CodeByHaamza |
| [`E1_020.json`](trad/dialogues/E1_020.json) | 67 | 67 | 100 % | terminé par @CodeByHaamza |
| [`E1_021.json`](trad/dialogues/E1_021.json) | 66 | 66 | 100 % | terminé par @vikmorp, @CodeByHaamza |
| [`E1_022.json`](trad/dialogues/E1_022.json) | 95 | 95 | 100 % | terminé par @Uolil-Raccoon, @CodeByHaamza |
| [`E1_023.json`](trad/dialogues/E1_023.json) | 96 | 96 | 100 % | terminé par @CodeByHaamza · 1 trop large |
| [`E1_024.json`](trad/dialogues/E1_024.json) | 93 | 93 | 100 % | terminé par @CodeByHaamza |
| [`E1_025.json`](trad/dialogues/E1_025.json) | 86 | 86 | 100 % | terminé par @Uolil-Raccoon, @CodeByHaamza |
| [`E1_026.json`](trad/dialogues/E1_026.json) | 97 | 97 | 100 % | terminé par @CodeByHaamza · 1 trop large |
| [`E1_027.json`](trad/dialogues/E1_027.json) | 89 | 89 | 100 % | terminé par @CodeByHaamza |
| [`E1_028.json`](trad/dialogues/E1_028.json) | 79 | 79 | 100 % | terminé par @CodeByHaamza |
| [`E1_029.json`](trad/dialogues/E1_029.json) | 99 | 99 | 100 % | terminé par @CodeByHaamza |
| [`E1_030.json`](trad/dialogues/E1_030.json) | 96 | 96 | 100 % | terminé par @CodeByHaamza |
| [`E1_031.json`](trad/dialogues/E1_031.json) | 97 | 97 | 100 % | terminé par @CodeByHaamza |
| [`E2_001.json`](trad/dialogues/E2_001.json) | 95 | 95 | 100 % | terminé par @CodeByHaamza · 1 trop large |
| [`E2_002.json`](trad/dialogues/E2_002.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`E2_003.json`](trad/dialogues/E2_003.json) | 96 | 96 | 100 % | terminé par @CodeByHaamza |
| [`E2_004.json`](trad/dialogues/E2_004.json) | 97 | 97 | 100 % | terminé par @CodeByHaamza |
| [`E2_005.json`](trad/dialogues/E2_005.json) | 92 | 92 | 100 % | terminé par @CodeByHaamza |
| [`E2_006.json`](trad/dialogues/E2_006.json) | 92 | 92 | 100 % | terminé par @CodeByHaamza |
| [`E2_007.json`](trad/dialogues/E2_007.json) | 99 | 99 | 100 % | terminé par @CodeByHaamza |
| [`E2_008.json`](trad/dialogues/E2_008.json) | 99 | 99 | 100 % | terminé par @CodeByHaamza |
| [`E2_009.json`](trad/dialogues/E2_009.json) | 97 | 97 | 100 % | terminé par @CodeByHaamza |
| [`E2_010.json`](trad/dialogues/E2_010.json) | 97 | 97 | 100 % | terminé par @CodeByHaamza |
| [`E2_011.json`](trad/dialogues/E2_011.json) | 90 | 90 | 100 % | terminé par @CodeByHaamza |
| [`E2_012.json`](trad/dialogues/E2_012.json) | 91 | 91 | 100 % | terminé par @CodeByHaamza |
| [`E2_013.json`](trad/dialogues/E2_013.json) | 88 | 88 | 100 % | terminé par @CodeByHaamza |
| [`E2_014.json`](trad/dialogues/E2_014.json) | 95 | 95 | 100 % | terminé par @CodeByHaamza |
| [`E2_015.json`](trad/dialogues/E2_015.json) | 91 | 91 | 100 % | terminé par @CodeByHaamza |
| [`E2_016.json`](trad/dialogues/E2_016.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`E2_017.json`](trad/dialogues/E2_017.json) | 80 | 80 | 100 % | terminé par @CodeByHaamza |
| [`E3_001.json`](trad/dialogues/E3_001.json) | 93 | 93 | 100 % | terminé par @CodeByHaamza |
| [`E3_002.json`](trad/dialogues/E3_002.json) | 97 | 97 | 100 % | terminé par @CodeByHaamza |
| [`E3_003.json`](trad/dialogues/E3_003.json) | 70 | 70 | 100 % | terminé par @CodeByHaamza |
| [`E3_004.json`](trad/dialogues/E3_004.json) | 95 | 95 | 100 % | terminé par @CodeByHaamza |
| [`E3_005.json`](trad/dialogues/E3_005.json) | 97 | 97 | 100 % | terminé par @CodeByHaamza |
| [`E3_006.json`](trad/dialogues/E3_006.json) | 98 | 98 | 100 % | terminé par @CodeByHaamza |
| [`E3_007.json`](trad/dialogues/E3_007.json) | 96 | 96 | 100 % | terminé par @Uolil-Raccoon, @CodeByHaamza · 1 trop large |
| [`E3_008.json`](trad/dialogues/E3_008.json) | 66 | 66 | 100 % | terminé par @CodeByHaamza |

## EBOOT

Prends un fichier **libre**, dis-le en ouvrant ta proposition, et il passera en « en cours » dans la minute.

| Fichier | Textes | Traduits | % | État |
|---|---:|---:|---:|---|
| [`EBOOT_001.json`](trad/eboot/EBOOT_001.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 5 à vérifier · relu (#136) |
| [`EBOOT_002.json`](trad/eboot/EBOOT_002.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 2 à vérifier · relu (#137) |
| [`EBOOT_003.json`](trad/eboot/EBOOT_003.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 15 à vérifier · relu (#138) |
| [`EBOOT_004.json`](trad/eboot/EBOOT_004.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 1 à vérifier |
| [`EBOOT_005.json`](trad/eboot/EBOOT_005.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`EBOOT_006.json`](trad/eboot/EBOOT_006.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`EBOOT_007.json`](trad/eboot/EBOOT_007.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`EBOOT_008.json`](trad/eboot/EBOOT_008.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`EBOOT_009.json`](trad/eboot/EBOOT_009.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`EBOOT_010.json`](trad/eboot/EBOOT_010.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 10 à vérifier |
| [`EBOOT_011.json`](trad/eboot/EBOOT_011.json) | 60 | 60 | 100 % | terminé par @CodeByHaamza · 5 à vérifier |
| [`EBOOT_012.json`](trad/eboot/EBOOT_012.json) | 58 | 58 | 100 % | terminé par @CodeByHaamza · 15 à vérifier |
| [`EBOOT_013.json`](trad/eboot/EBOOT_013.json) | 82 | 82 | 100 % | terminé par @CodeByHaamza · 5 à vérifier |
| [`EBOOT_014.json`](trad/eboot/EBOOT_014.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 20 à vérifier |
| [`EBOOT_015.json`](trad/eboot/EBOOT_015.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 21 à vérifier |
| [`EBOOT_016.json`](trad/eboot/EBOOT_016.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 7 à vérifier |
| [`EBOOT_017.json`](trad/eboot/EBOOT_017.json) | 18 | 18 | 100 % | terminé par @CodeByHaamza · 1 à vérifier |
| [`EBOOT_018.json`](trad/eboot/EBOOT_018.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 16 à vérifier |
| [`EBOOT_019.json`](trad/eboot/EBOOT_019.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 8 à vérifier |
| [`EBOOT_020.json`](trad/eboot/EBOOT_020.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 3 à vérifier |
| [`EBOOT_021.json`](trad/eboot/EBOOT_021.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 25 à vérifier |
| [`EBOOT_022.json`](trad/eboot/EBOOT_022.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 2 à vérifier |
| [`EBOOT_023.json`](trad/eboot/EBOOT_023.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 4 à vérifier |
| [`EBOOT_024.json`](trad/eboot/EBOOT_024.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 1 à vérifier |
| [`EBOOT_025.json`](trad/eboot/EBOOT_025.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 10 à vérifier |
| [`EBOOT_026.json`](trad/eboot/EBOOT_026.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 23 à vérifier |
| [`EBOOT_027.json`](trad/eboot/EBOOT_027.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 16 à vérifier |
| [`EBOOT_028.json`](trad/eboot/EBOOT_028.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 17 à vérifier |
| [`EBOOT_029.json`](trad/eboot/EBOOT_029.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 22 à vérifier |
| [`EBOOT_030.json`](trad/eboot/EBOOT_030.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 29 à vérifier |
| [`EBOOT_031.json`](trad/eboot/EBOOT_031.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 5 à vérifier |
| [`EBOOT_032.json`](trad/eboot/EBOOT_032.json) | 38 | 38 | 100 % | terminé par @CodeByHaamza · 2 à vérifier |

## Donjons

Prends un fichier **libre**, dis-le en ouvrant ta proposition, et il passera en « en cours » dans la minute.

| Fichier | Textes | Traduits | % | État |
|---|---:|---:|---:|---|
| [`DNG_001.json`](trad/donjons/DNG_001.json) | 99 | 99 | 100 % | terminé par @CodeByHaamza · 2 trop large |
| [`DNG_002.json`](trad/donjons/DNG_002.json) | 31 | 31 | 100 % | terminé par @CodeByHaamza |

## Négociations

Prends un fichier **libre**, dis-le en ouvrant ta proposition, et il passera en « en cours » dans la minute.

| Fichier | Textes | Traduits | % | État |
|---|---:|---:|---:|---|
| [`ALIEN_001.json`](trad/negociations/ALIEN_001.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`ALIEN_002.json`](trad/negociations/ALIEN_002.json) | 5 | 5 | 100 % | terminé par @CodeByHaamza |
| [`BASKET_001.json`](trad/negociations/BASKET_001.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`BASKET_002.json`](trad/negociations/BASKET_002.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`BASKET_003.json`](trad/negociations/BASKET_003.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`BASKET_004.json`](trad/negociations/BASKET_004.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`BASKET_005.json`](trad/negociations/BASKET_005.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`BASKET_006.json`](trad/negociations/BASKET_006.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 1 à alléger |
| [`BASKET_007.json`](trad/negociations/BASKET_007.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 1 à alléger |
| [`BASKET_008.json`](trad/negociations/BASKET_008.json) | 56 | 56 | 100 % | terminé par @CodeByHaamza |
| [`DOPPEL_001.json`](trad/negociations/DOPPEL_001.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`DOPPEL_002.json`](trad/negociations/DOPPEL_002.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`DOPPEL_003.json`](trad/negociations/DOPPEL_003.json) | 14 | 14 | 100 % | terminé par @CodeByHaamza |
| [`ETC_001.json`](trad/negociations/ETC_001.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`ETC_002.json`](trad/negociations/ETC_002.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`ETC_003.json`](trad/negociations/ETC_003.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`ETC_004.json`](trad/negociations/ETC_004.json) | 24 | 24 | 100 % | terminé par @CodeByHaamza |
| [`GAKI_001.json`](trad/negociations/GAKI_001.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`GAKI_002.json`](trad/negociations/GAKI_002.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`GAKI_003.json`](trad/negociations/GAKI_003.json) | 28 | 28 | 100 % | terminé par @CodeByHaamza |
| [`HIHO_001.json`](trad/negociations/HIHO_001.json) | 100 | 100 | 100 % | terminé par @ATMC14 |
| [`HIHO_002.json`](trad/negociations/HIHO_002.json) | 100 | 100 | 100 % | terminé par @ATMC14 |
| [`HIHO_003.json`](trad/negociations/HIHO_003.json) | 100 | 100 | 100 % | terminé par @ATMC14 |
| [`HIHO_004.json`](trad/negociations/HIHO_004.json) | 100 | 100 | 100 % | terminé par @ATMC14 |
| [`HIHO_005.json`](trad/negociations/HIHO_005.json) | 100 | 100 | 100 % | terminé par @ATMC14, @CodeByHaamza |
| [`HIHO_006.json`](trad/negociations/HIHO_006.json) | 100 | 100 | 100 % | terminé par @ATMC14 |
| [`HIHO_007.json`](trad/negociations/HIHO_007.json) | 68 | 68 | 100 % | terminé par @ATMC14, @CodeByHaamza |
| [`KEMONO_001.json`](trad/negociations/KEMONO_001.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`KEMONO_002.json`](trad/negociations/KEMONO_002.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`KEMONO_003.json`](trad/negociations/KEMONO_003.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`KEMONO_004.json`](trad/negociations/KEMONO_004.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 1 à relire |
| [`KEMONO_005.json`](trad/negociations/KEMONO_005.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 1 à relire |
| [`KEMONO_006.json`](trad/negociations/KEMONO_006.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 1 à relire |
| [`KEMONO_007.json`](trad/negociations/KEMONO_007.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 1 trop large |
| [`KEMONO_008.json`](trad/negociations/KEMONO_008.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`KEMONO_009.json`](trad/negociations/KEMONO_009.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`KEMONO_010.json`](trad/negociations/KEMONO_010.json) | 69 | 69 | 100 % | terminé par @CodeByHaamza |
| [`KOKURI_001.json`](trad/negociations/KOKURI_001.json) | 96 | 96 | 100 % | terminé par @ATMC14, @CodeByHaamza · 1 trop large |
| [`KOROU_001.json`](trad/negociations/KOROU_001.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`KOROU_002.json`](trad/negociations/KOROU_002.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 1 à alléger |
| [`KOROU_003.json`](trad/negociations/KOROU_003.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 1 à relire |
| [`KOROU_004.json`](trad/negociations/KOROU_004.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 1 à relire |
| [`KOROU_005.json`](trad/negociations/KOROU_005.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 1 à relire |
| [`KOROU_006.json`](trad/negociations/KOROU_006.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`KOROU_007.json`](trad/negociations/KOROU_007.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`KOROU_008.json`](trad/negociations/KOROU_008.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`KOROU_009.json`](trad/negociations/KOROU_009.json) | 69 | 69 | 100 % | terminé par @CodeByHaamza |
| [`KOSIKI_001.json`](trad/negociations/KOSIKI_001.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`KOSIKI_002.json`](trad/negociations/KOSIKI_002.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`KOSIKI_003.json`](trad/negociations/KOSIKI_003.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`KOSIKI_004.json`](trad/negociations/KOSIKI_004.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`KOSIKI_005.json`](trad/negociations/KOSIKI_005.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`KOSIKI_006.json`](trad/negociations/KOSIKI_006.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`KOSIKI_007.json`](trad/negociations/KOSIKI_007.json) | 25 | 25 | 100 % | terminé par @CodeByHaamza |
| [`KOUMAN_001.json`](trad/negociations/KOUMAN_001.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 2 à alléger |
| [`KOUMAN_002.json`](trad/negociations/KOUMAN_002.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`KOUMAN_003.json`](trad/negociations/KOUMAN_003.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`KOUMAN_004.json`](trad/negociations/KOUMAN_004.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`KOUMAN_005.json`](trad/negociations/KOUMAN_005.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`KOUMAN_006.json`](trad/negociations/KOUMAN_006.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`KOUMAN_007.json`](trad/negociations/KOUMAN_007.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 1 à relire |
| [`KOUMAN_008.json`](trad/negociations/KOUMAN_008.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`KOUMAN_009.json`](trad/negociations/KOUMAN_009.json) | 93 | 93 | 100 % | terminé par @CodeByHaamza |
| [`KUTISAKE_001.json`](trad/negociations/KUTISAKE_001.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`KUTISAKE_002.json`](trad/negociations/KUTISAKE_002.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`KUTISAKE_003.json`](trad/negociations/KUTISAKE_003.json) | 81 | 81 | 100 % | terminé par @CodeByHaamza |
| [`KYOUKI_001.json`](trad/negociations/KYOUKI_001.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`KYOUKI_002.json`](trad/negociations/KYOUKI_002.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`KYOUKI_003.json`](trad/negociations/KYOUKI_003.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`KYOUKI_004.json`](trad/negociations/KYOUKI_004.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`KYOUKI_005.json`](trad/negociations/KYOUKI_005.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`KYOUKI_006.json`](trad/negociations/KYOUKI_006.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`KYOUKI_007.json`](trad/negociations/KYOUKI_007.json) | 23 | 23 | 100 % | terminé par @CodeByHaamza |
| [`MAYOERU_001.json`](trad/negociations/MAYOERU_001.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`MAYOERU_002.json`](trad/negociations/MAYOERU_002.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`MAYOERU_003.json`](trad/negociations/MAYOERU_003.json) | 39 | 39 | 100 % | terminé par @CodeByHaamza |
| [`POLUTAR_001.json`](trad/negociations/POLUTAR_001.json) | 100 | 100 | 100 % | terminé par @ATMC14 |
| [`POLUTAR_002.json`](trad/negociations/POLUTAR_002.json) | 100 | 100 | 100 % | terminé par @ATMC14 |
| [`POLUTAR_003.json`](trad/negociations/POLUTAR_003.json) | 100 | 100 | 100 % | terminé par @ATMC14 |
| [`POLUTAR_004.json`](trad/negociations/POLUTAR_004.json) | 36 | 36 | 100 % | terminé par @ATMC14 |
| [`QSIRUBA_001.json`](trad/negociations/QSIRUBA_001.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`QSIRUBA_002.json`](trad/negociations/QSIRUBA_002.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`QSIRUBA_003.json`](trad/negociations/QSIRUBA_003.json) | 20 | 20 | 100 % | terminé par @CodeByHaamza |
| [`SINSI_001.json`](trad/negociations/SINSI_001.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`SINSI_002.json`](trad/negociations/SINSI_002.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`SINSI_003.json`](trad/negociations/SINSI_003.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 2 à alléger |
| [`SINSI_004.json`](trad/negociations/SINSI_004.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`SINSI_005.json`](trad/negociations/SINSI_005.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`SINSI_006.json`](trad/negociations/SINSI_006.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`SINSI_007.json`](trad/negociations/SINSI_007.json) | 36 | 36 | 100 % | terminé par @CodeByHaamza |
| [`SLIME_001.json`](trad/negociations/SLIME_001.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`SLIME_002.json`](trad/negociations/SLIME_002.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`SLIME_003.json`](trad/negociations/SLIME_003.json) | 20 | 20 | 100 % | terminé par @CodeByHaamza |
| [`SYOUJO_001.json`](trad/negociations/SYOUJO_001.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 1 à alléger |
| [`SYOUJO_002.json`](trad/negociations/SYOUJO_002.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 1 à alléger |
| [`SYOUJO_003.json`](trad/negociations/SYOUJO_003.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 1 à alléger |
| [`SYOUJO_004.json`](trad/negociations/SYOUJO_004.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`SYOUJO_005.json`](trad/negociations/SYOUJO_005.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 4 à alléger |
| [`SYOUJO_006.json`](trad/negociations/SYOUJO_006.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 4 à alléger |
| [`SYOUJO_007.json`](trad/negociations/SYOUJO_007.json) | 9 | 9 | 100 % | terminé par @Uolil-Raccoon |
| [`TENSI_001.json`](trad/negociations/TENSI_001.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`TENSI_002.json`](trad/negociations/TENSI_002.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`TENSI_003.json`](trad/negociations/TENSI_003.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`TENSI_004.json`](trad/negociations/TENSI_004.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`TENSI_005.json`](trad/negociations/TENSI_005.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`TENSI_006.json`](trad/negociations/TENSI_006.json) | 82 | 82 | 100 % | terminé par @CodeByHaamza |
| [`TINPRA_001.json`](trad/negociations/TINPRA_001.json) | 100 | 100 | 100 % | terminé par @ATMC14, @CodeByHaamza |
| [`TINPRA_002.json`](trad/negociations/TINPRA_002.json) | 100 | 100 | 100 % | terminé par @ATMC14 |
| [`TINPRA_003.json`](trad/negociations/TINPRA_003.json) | 69 | 69 | 100 % | terminé par @ATMC14 |
| [`TOILET_001.json`](trad/negociations/TOILET_001.json) | 100 | 100 | 100 % | terminé par @Uolil-Raccoon, @CodeByHaamza · 1 à alléger |
| [`TOILET_002.json`](trad/negociations/TOILET_002.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`TOILET_003.json`](trad/negociations/TOILET_003.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`TOILET_004.json`](trad/negociations/TOILET_004.json) | 19 | 19 | 100 % | terminé par @Uolil-Raccoon |
| [`WORM_001.json`](trad/negociations/WORM_001.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`WORM_002.json`](trad/negociations/WORM_002.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`WORM_003.json`](trad/negociations/WORM_003.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`WORM_004.json`](trad/negociations/WORM_004.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`WORM_005.json`](trad/negociations/WORM_005.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`WORM_006.json`](trad/negociations/WORM_006.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`WORM_007.json`](trad/negociations/WORM_007.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`WORM_008.json`](trad/negociations/WORM_008.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`WORM_009.json`](trad/negociations/WORM_009.json) | 86 | 86 | 100 % | terminé par @CodeByHaamza |
| [`WTENSI_001.json`](trad/negociations/WTENSI_001.json) | 80 | 80 | 100 % | terminé par @ATMC14 |
| [`YAKUZA_001.json`](trad/negociations/YAKUZA_001.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`YAKUZA_002.json`](trad/negociations/YAKUZA_002.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`YAKUZA_003.json`](trad/negociations/YAKUZA_003.json) | 59 | 59 | 100 % | terminé par @CodeByHaamza |
| [`YOUEN_001.json`](trad/negociations/YOUEN_001.json) | 100 | 100 | 100 % | terminé par @ATMC14 |
| [`YOUEN_002.json`](trad/negociations/YOUEN_002.json) | 100 | 100 | 100 % | terminé par @ATMC14 |
| [`YOUEN_003.json`](trad/negociations/YOUEN_003.json) | 100 | 100 | 100 % | terminé par @ATMC14, @CodeByHaamza |
| [`YOUEN_004.json`](trad/negociations/YOUEN_004.json) | 100 | 100 | 100 % | terminé par @ATMC14 |
| [`YOUEN_005.json`](trad/negociations/YOUEN_005.json) | 100 | 100 | 100 % | terminé par @ATMC14 |
| [`YOUEN_006.json`](trad/negociations/YOUEN_006.json) | 87 | 87 | 100 % | terminé par @ATMC14 |
| [`ZMBITYAN_001.json`](trad/negociations/ZMBITYAN_001.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`ZMBITYAN_002.json`](trad/negociations/ZMBITYAN_002.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`ZMBITYAN_003.json`](trad/negociations/ZMBITYAN_003.json) | 22 | 22 | 100 % | terminé par @CodeByHaamza |
| [`ZOMBIKO_001.json`](trad/negociations/ZOMBIKO_001.json) | 100 | 100 | 100 % | terminé par @ATMC14 |
| [`ZOMBIKO_002.json`](trad/negociations/ZOMBIKO_002.json) | 90 | 90 | 100 % | terminé par @ATMC14, @CodeByHaamza |
| [`ZOMB_MAN_001.json`](trad/negociations/ZOMB_MAN_001.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza |
| [`ZOMB_MAN_002.json`](trad/negociations/ZOMB_MAN_002.json) | 82 | 82 | 100 % | terminé par @vikmorp, @CodeByHaamza |

## Noms

Prends un fichier **libre**, dis-le en ouvrant ta proposition, et il passera en « en cours » dans la minute.

| Fichier | Textes | Traduits | % | État |
|---|---:|---:|---:|---|
| [`ARMES_001.json`](trad/noms/ARMES_001.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · 1 trop large · relu (#131) |
| [`ARMES_002.json`](trad/noms/ARMES_002.json) | 2 | 2 | 100 % | terminé par @CodeByHaamza · relu (#132) |
| [`ARMURES_001.json`](trad/noms/ARMURES_001.json) | 65 | 65 | 100 % | terminé par @CodeByHaamza |
| [`OBJETS_001.json`](trad/noms/OBJETS_001.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · relu (#134) |
| [`OBJETS_002.json`](trad/noms/OBJETS_002.json) | 54 | 54 | 100 % | terminé par @CodeByHaamza · 1 trop large · relu (#135) |
| [`SORTS_001.json`](trad/noms/SORTS_001.json) | 100 | 100 | 100 % | terminé par @CodeByHaamza · relu (#128) |
| [`SORTS_002.json`](trad/noms/SORTS_002.json) | 18 | 18 | 100 % | terminé par @CodeByHaamza · relu (#129) |

