import subprocess

def test_mabeData2StdPhylogeny_CmdLine():
    cmd = "python3 mabeData2stdPhylogeny.py"
    path = "example_data/example_mabe_output_asexual/snapshot_data/"
    subprocess.run(f"{cmd} -path {path}", shell=True)
    subprocess.run("rm lineage.csv", shell=True)

if __name__ == "__main__":
    test_mabeData2StdPhylogeny_CmdLine()