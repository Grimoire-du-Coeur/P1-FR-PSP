"""Génère les visuels animés du README : bannière et séparateur.

    python game/public/assets/_src/gen_visuels.py   # -> game/public/assets/banniere.svg, separateur.svg

Thème : la jaquette PSP de Shin Megami Tensei: Persona. Ciel lavande et
brume qui dérive, lune voilée, papillons de Philémon qui volent, éventail
de cartes de tarot (les Arcanes) qui ondule, titre fin et lumineux ; ruban
tricolore du Grimoire du Cœur.

Le texte est vectorisé (fontTools + polices Windows) : GitHub sert les SVG
du README via <img>, ce qui bloque toute police externe, et un <text>
vivant s'afficherait différemment selon l'OS. Les animations sont en CSS ;
avec « réduire les animations », tout s'affiche à l'arrêt.

Dépendance de développement : fontTools (pip install fonttools).
"""

# Les gabarits SVG ci-dessous sont des lignes longues par nature : les couper
# changerait le fichier produit.
# ruff: noqa: E501

from __future__ import annotations

import random
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

ASSETS = Path(__file__).resolve().parent.parent
POLICES = Path("C:/Windows/Fonts")

ENCRE = "#0D0D0D"
BLANC = "#F5F5F5"
BLEU_GRIMOIRE, ROUGE_GRIMOIRE = "#002654", "#CE1126"
LAVANDE, LAVANDE_PALE, VIOLET, NUIT = "#B9A6D6", "#E8E0F5", "#5B3F8C", "#140A24"
OR, OR_PALE, BLEU_PAPILLON = "#D9B66A", "#F3DFA8", "#7FB4FF"


class Police:
    def __init__(self, fichier: str):
        self.f = TTFont(POLICES / fichier)
        self.glyphes = self.f.getGlyphSet()
        self.cmap = self.f.getBestCmap()
        self.em = self.f["head"].unitsPerEm

    def largeur(self, texte: str, taille: float, espacement: float = 0) -> float:
        k = taille / self.em
        return sum(self.glyphes[self.cmap[ord(c)]].width * k + espacement for c in texte) - espacement

    def chemin(self, texte: str, x: float, y: float, taille: float, espacement: float = 0) -> str:
        k = taille / self.em
        morceaux = []
        for c in texte:
            nom = self.cmap[ord(c)]
            stylo = SVGPathPen(self.glyphes)
            self.glyphes[nom].draw(TransformPen(stylo, (k, 0, 0, -k, x, y)))
            morceaux.append(stylo.getCommands())
            x += self.glyphes[nom].width * k + espacement
        return " ".join(m for m in morceaux if m)

    def centre(self, texte: str, cx: float, y: float, taille: float, espacement: float = 0) -> str:
        return self.chemin(texte, cx - self.largeur(texte, taille, espacement) / 2, y, taille, espacement)


def _n(v: float) -> str:
    return f"{v:.1f}".rstrip("0").rstrip(".")


def papillon(classe: str, x: float, y: float, echelle: float, couleur: str, angle: float) -> str:
    aile = (
        f'<path d="M0 0 C-20 -24 -36 -6 -24 8 C-16 17 -5 9 0 2 Z" fill="{couleur}"/>'
        f'<path d="M0 2 C-7 15 -20 24 -13 30 C-5 33 -1 18 0 5 Z" fill="{couleur}" opacity=".75"/>'
    )
    ailes = aile + aile.replace(
        "M0 0 C-20 -24 -36 -6 -24 8 C-16 17 -5 9 0 2 Z", "M0 0 C20 -24 36 -6 24 8 C16 17 5 9 0 2 Z"
    ).replace("M0 2 C-7 15 -20 24 -13 30 C-5 33 -1 18 0 5 Z", "M0 2 C7 15 20 24 13 30 C5 33 1 18 0 5 Z")
    return (
        f'<g class="{classe}"><g transform="translate({_n(x)} {_n(y)}) rotate({_n(angle)}) scale({echelle})">'
        f'<g class="ailes">{ailes}</g>'
        f'<rect x="-1.4" y="-7" width="2.8" height="20" rx="1.4" fill="{NUIT}"/></g></g>'
    )


def carte_tarot(i: int, n: int) -> str:
    angle = (i - (n - 1) / 2) * 9
    return (
        f'<g transform="translate(0 22) rotate({_n(angle)} 600 560)"><g class="carte c{i}">'
        f'<rect x="572" y="330" width="56" height="88" rx="6" fill="#241338" stroke="{OR}" stroke-width="1.6"/>'
        f'<rect x="578" y="336" width="44" height="76" rx="3" fill="none" stroke="{OR}" stroke-width=".8" opacity=".6"/>'
        f'<circle cx="600" cy="374" r="11" fill="none" stroke="{OR}" stroke-width="1"/>'
        f'<path d="M600 361 L603 371 L613 374 L603 377 L600 387 L597 377 L587 374 L597 371 Z" fill="{OR}" opacity=".85"/>'
        f"</g></g>"
    )


def banniere() -> str:
    W, H = 1200, 440
    fine = Police("segoeuil.ttf")  # Segoe UI Light
    grasse = Police("segoeuib.ttf")  # Segoe UI Bold
    rnd = random.Random(1996)  # sortie japonaise de Megami Ibunroku Persona

    sur_titre = grasse.centre("SHIN MEGAMI TENSEI", 600, 108, 24, 9)
    titre = fine.centre("Persona", 600, 222, 132, 2)
    sous_titre = grasse.centre("TRADUCTION FRANÇAISE  ·  PSP", 600, 270, 20, 4)
    grimoire = grasse.centre("GRIMOIRE DU CŒUR", 600, 320, 13, 5)

    etoiles = "".join(
        f'<circle class="e{rnd.randrange(3)}" cx="{_n(rnd.uniform(10, 1190))}" cy="{_n(rnd.uniform(8, 300))}" '
        f'r="{_n(rnd.uniform(0.6, 1.6))}" fill="{LAVANDE_PALE}"/>'
        for _ in range(70)
    )
    brume = "".join(
        f'<ellipse cx="{_n(x)}" cy="{_n(y)}" rx="{_n(rx)}" ry="{_n(ry)}" fill="{LAVANDE_PALE}" opacity="{_n(o)}"/>'
        for x, y, rx, ry, o in (
            (
                rnd.uniform(-100, 1300),
                rnd.uniform(240, 420),
                rnd.uniform(160, 320),
                rnd.uniform(30, 60),
                rnd.uniform(0.05, 0.12),
            )
            for _ in range(14)
        )
    )
    cartes = "".join(carte_tarot(i, 7) for i in range(7))
    vols = "".join(
        [
            papillon("p1", 238, 150, 0.9, BLEU_PAPILLON, -16),
            papillon("p2", 968, 120, 0.7, LAVANDE_PALE, 14),
            papillon("p3", 1050, 300, 0.55, OR_PALE, 8),
            papillon("p4", 140, 330, 0.5, BLEU_PAPILLON, -6),
        ]
    )

    style = (
        "<style>"
        ".e0,.e1,.e2{animation:scintille 3.4s ease-in-out infinite}.e1{animation-delay:-1.2s}.e2{animation-delay:-2.3s}"
        "@keyframes scintille{50%{opacity:.15}}"
        ".brume{animation:derive 26s linear infinite alternate}.brume2{animation-duration:34s;animation-direction:alternate-reverse}"
        "@keyframes derive{from{transform:translateX(-60px)}to{transform:translateX(60px)}}"
        ".lune{animation:pulse 6s ease-in-out infinite}@keyframes pulse{50%{opacity:.55}}"
        ".ailes{transform-box:fill-box;transform-origin:50% 50%;animation:bat .55s ease-in-out infinite alternate}"
        "@keyframes bat{to{transform:scaleX(.3)}}"
        ".p1{animation:vol1 9s ease-in-out infinite}.p2{animation:vol2 11s ease-in-out infinite}"
        ".p3{animation:vol1 13s ease-in-out -4s infinite}.p4{animation:vol2 10s ease-in-out -2s infinite}"
        "@keyframes vol1{50%{transform:translate(26px,-18px)}}@keyframes vol2{50%{transform:translate(-22px,14px)}}"
        ".carte{transform-box:fill-box;transform-origin:50% 100%;animation:ondule 5s ease-in-out infinite}"
        + "".join(f".c{i}{{animation-delay:-{i * 0.45:.2f}s}}" for i in range(7))
        + "@keyframes ondule{50%{transform:translateY(-8px)}}"
        ".reflet{animation:reflet 6s ease-in-out 1s infinite}"
        "@keyframes reflet{0%{transform:translateX(-300px)}50%,100%{transform:translateX(1500px)}}"
        "@media (prefers-reduced-motion:reduce){*{animation:none!important}.reflet{opacity:0}}"
        "</style>"
    )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d">
<title id="t">Shin Megami Tensei: Persona — traduction française (PSP)</title>
<desc id="d">Bannière : ciel lavande et brume, papillons, éventail de cartes de tarot, titre « Persona ».</desc>
<defs>
<linearGradient id="ciel" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{NUIT}"/><stop offset=".55" stop-color="#3A2363"/><stop offset="1" stop-color="#8E78B8"/></linearGradient>
<radialGradient id="halo" cx="50%" cy="46%" r="45%"><stop offset="0" stop-color="{LAVANDE_PALE}" stop-opacity=".35"/><stop offset="1" stop-color="{LAVANDE_PALE}" stop-opacity="0"/></radialGradient>
<radialGradient id="lune" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".9"/><stop offset=".6" stop-color="{LAVANDE_PALE}" stop-opacity=".5"/><stop offset="1" stop-color="{LAVANDE_PALE}" stop-opacity="0"/></radialGradient>
<linearGradient id="titre" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="{LAVANDE_PALE}"/></linearGradient>
<linearGradient id="balayage" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".6"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<filter id="lueur" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="flou" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="18"/></filter>
<clipPath id="lettres"><path d="{titre}"/></clipPath>
</defs>
{style}
<rect width="{W}" height="{H}" fill="url(#ciel)"/>
{etoiles}
<circle class="lune" cx="930" cy="92" r="64" fill="url(#lune)"/>
<rect width="{W}" height="{H}" fill="url(#halo)"/>
<g class="brume" filter="url(#flou)">{brume}</g>
<path d="{sur_titre}" fill="{OR_PALE}"/>
<path d="{titre}" fill="url(#titre)" filter="url(#lueur)"/>
<g clip-path="url(#lettres)"><rect class="reflet" x="0" y="100" width="180" height="140" fill="url(#balayage)" transform="skewX(-20)"/></g>
<rect x="430" y="240" width="340" height="1.2" fill="{OR}" opacity=".7"/>
<path d="{sous_titre}" fill="{OR_PALE}"/>
<rect x="531" y="290" width="46" height="7" fill="{BLEU_GRIMOIRE}"/><rect x="577" y="290" width="46" height="7" fill="{BLANC}"/><rect x="623" y="290" width="46" height="7" fill="{ROUGE_GRIMOIRE}"/>
<path d="{grimoire}" fill="{BLANC}" opacity=".85"/>
<g class="brume brume2" filter="url(#flou)" opacity=".8">{brume}</g>
{cartes}
{vols}
</svg>
"""


def separateur() -> str:
    W, H = 1200, 40
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="séparateur">
<defs>
<linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="{LAVANDE}" stop-opacity="0"/><stop offset=".4" stop-color="{LAVANDE}"/><stop offset=".5" stop-color="{OR}"/><stop offset=".6" stop-color="{LAVANDE}"/><stop offset="1" stop-color="{LAVANDE}" stop-opacity="0"/></linearGradient>
<linearGradient id="r" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#FFF4D6" stop-opacity=".9"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<clipPath id="c"><rect x="0" y="19" width="{W}" height="2"/></clipPath>
</defs>
<style>.b{{animation:b 5s ease-in-out infinite}}@keyframes b{{0%{{transform:translateX(-200px)}}60%,100%{{transform:translateX(1300px)}}}}.ailes{{transform-box:fill-box;transform-origin:50% 50%;animation:bat .6s ease-in-out infinite alternate}}@keyframes bat{{to{{transform:scaleX(.3)}}}}@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}.b{{opacity:0}}}}</style>
<rect x="0" y="19" width="{W}" height="2" fill="url(#g)"/>
<g clip-path="url(#c)"><rect class="b" x="0" y="19" width="180" height="2" fill="url(#r)"/></g>
<rect x="572" y="15" width="56" height="10" rx="5" fill="#140A24" opacity=".0"/>
{papillon("pp", 600, 16, 0.55, BLEU_PAPILLON, 0)}
</svg>
"""


if __name__ == "__main__":
    (ASSETS / "banniere.svg").write_text(banniere(), encoding="utf-8", newline="\n")
    (ASSETS / "separateur.svg").write_text(separateur(), encoding="utf-8", newline="\n")
    print("banniere.svg et separateur.svg générés")
