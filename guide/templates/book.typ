// The Games Master's guide as a book. A pandoc template: $$body$$ is the whole
// guide, converted from markdown; stat blocks, scene cards and boxed text arrive
// as raw Typst that calls the functions defined here.

#let tdmred = rgb("#7a1c12")
#let sbhead = rgb("#d8c7a3")
#let sbrule = rgb("#8a7a5a")
#let boxfill = rgb("#ece0c6")

#set document(title: "$book$")
#set page(paper: "us-letter", margin: (x: 0.85in, y: 0.9in), fill: rgb("#fbf7ef"),
  footer: context [
    #set text(size: 8pt, fill: sbrule)
    #h(1fr) #counter(page).display() #h(1fr)
  ])
#set text(font: ("Libertinus Serif", "New Computer Modern"), size: 10.5pt, fill: rgb("#2a2118"), lang: "en")
#set par(justify: true, leading: 0.62em, spacing: 0.9em)

#show heading: set text(fill: tdmred)
#show heading.where(level: 1): it => { pagebreak(weak: true); block(below: 1em)[#set text(size: 22pt); #smallcaps(it.body) #line(length: 100%, stroke: 1.2pt + tdmred)] }
#show heading.where(level: 2): set text(size: 15pt)
#show heading.where(level: 3): it => block(above: 1.2em, below: 0.6em)[#set text(size: 12pt); #smallcaps(it.body)]
#show heading.where(level: 4): set text(size: 11pt)

#set table(stroke: 0.4pt + sbrule, inset: 4pt)
#show table: set text(size: 8.5pt)
#show table: set par(justify: false)
#show figure.where(kind: table): set figure.caption(position: top)
#show figure: set block(breakable: true)

#let horizontalrule = line(start: (25%,0%), end: (75%,0%), stroke: 0.5pt + sbrule)

#let sbtable(columns: auto, ..cells) = block(breakable: false, width: 100%, above: 0.4em, below: 0.2em)[
  #table(columns: columns, ..cells)
]

#let scenecard(..rows) = block(breakable: false, below: 1em)[
  #table(columns: (auto, 1fr),
    ..rows.pos().map(r => (table.cell(fill: sbhead)[*#r.at(0)*], [#r.at(1)])).flatten())
]

#let tdmbox(body) = block(fill: boxfill, stroke: (left: 3pt + tdmred, rest: 0.4pt + sbrule),
  inset: 9pt, width: 100%, breakable: true)[#body]

// Title page
#page(margin: 1in)[
  #v(2.2in)
  #align(center)[
    #text(size: 30pt, fill: tdmred, hyphenate: false)[#smallcaps[$book$]]
    #v(0.4em)
    #line(length: 60%, stroke: 1.2pt + tdmred)
    #v(0.6em)
    #text(size: 13pt, style: "italic")[A Games Master's Guide for _Classic Fantasy Imperative_]
    #v(3in)
    #text(size: 9pt, fill: sbrule)[Fourth Wall Gaming]
  ]
]

#outline(title: [Contents], depth: 2, indent: auto)

$body$
