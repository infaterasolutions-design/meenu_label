import os

workspace = r'c:\Users\sande\Documents\antigravity\splendid-nobel'
scratch = os.path.join(workspace, 'scratch')

for f in os.listdir(scratch):
    if f.startswith('temp_snitch') or f.startswith('test_pdp_snitch'):
        full = os.path.join(scratch, f)
        try:
            if os.path.isfile(full):
                os.remove(full)
                print("Removed:", f)
        except:
            pass

print("Cleaned up temp snitch preview files.")
