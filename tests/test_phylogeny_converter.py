import subprocess
import mabe_converters as mc

def test_mabeData2StdPhylogeny_CmdLine():
    cmd = "python3 mabe_converters/phylogeny.py"
    path = "example_data/example_mabe_output_asexual/snapshot_data/"
    subprocess.run(f"{cmd} -path {path}", shell=True)
    subprocess.run("rm lineage.csv", shell=True)

def test_ConverterFunction():
    mc.ConvertMABESnapshotsToStdPhylogeny("example_data/example_mabe_output_asexual/snapshot_data/")
    subprocess.run("rm lineage.csv", shell=True)

if __name__ == "__main__":
    test_mabeData2StdPhylogeny_CmdLine()
    test_ConverterFunction()