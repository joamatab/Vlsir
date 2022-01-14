"""
# Vlsir Bindings Unit Tests 
"""

# Import the package under test 
import vlsir


def test_version():
    assert vlsir.__version__ == "0.2.0"


def test_sim():
    inp = vlsir.spice.SimInput()
    inp.pkg.modules.append(
        vlsir.circuit.Module(
            name="top",
            ports=[
                vlsir.circuit.Port(
                    direction="NONE", signal=vlsir.circuit.Signal(name="VSS", width=1)
                )
            ],
            signals=[vlsir.circuit.Signal(name="1", width=1)],
            instances=[
                vlsir.circuit.Instance(
                    name="r1",
                    module=vlsir.utils.Reference(
                        external=vlsir.utils.QualifiedName(
                            domain="hdl21.ideal", name="IdealResistor"
                        )
                    ),
                    connections=dict(
                        p=vlsir.circuit.Connection(
                            sig=vlsir.circuit.Signal(name="1", width=1)
                        ),
                        n=vlsir.circuit.Connection(
                            sig=vlsir.circuit.Signal(name="VSS", width=1)
                        ),
                    ),
                )
            ],
        )
    )
    inp.top = "top"

