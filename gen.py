#!/usr/bin/env python3

groups = range(1,8)

code = "lelo"
template = """

GR0{g}: [repos](https://github.com/analogicus/{code}_gr0{g}_sky130a) [docs](https://analogicus.github.io/{code}_gr0{g}_sky130a)
[![GDS](https://github.com/analogicus/{code}_gr0{g}_sky130a/actions/workflows/gds.yaml/badge.svg)](https://github.com/analogicus/{code}_gr0{g}_sky130a/actions/workflows/gds.yaml)
[![DRC](https://github.com/analogicus/{code}_gr0{g}_sky130a/actions/workflows/drc.yaml/badge.svg)](https://github.com/analogicus/{code}_gr0{g}_sky130a/actions/workflows/drc.yaml)
[![LVS](https://github.com/analogicus/{code}_gr0{g}_sky130a/actions/workflows/lvs.yaml/badge.svg)](https://github.com/analogicus/{code}_gr0{g}_sky130a/actions/workflows/lvs.yaml)
[![DOCS](https://github.com/analogicus/{code}_gr0{g}_sky130a/actions/workflows/docs.yaml/badge.svg)](https://github.com/analogicus/{code}_gr0{g}_sky130a/actions/workflows/docs.yaml)
[![SIM](https://github.com/analogicus/{code}_gr0{g}_sky130a/actions/workflows/sim.yaml/badge.svg)](https://github.com/analogicus/{code}_gr0{g}_sky130a/actions/workflows/sim.yaml)

"""

with open("README.md","w") as fo:
    for g in groups:
        fo.write(template.replace("{code}",code).replace("{g}",str(g)))
