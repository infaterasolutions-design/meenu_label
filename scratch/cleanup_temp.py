import os

workspace = r'c:\Users\sande\Documents\antigravity\splendid-nobel'
scratch = os.path.join(workspace, 'scratch')

for f in os.listdir(scratch):
    if f.startswith('temp_') or f.startswith('render_pdp_') or f.startswith('pdp_preview_') or f.startswith('snap_pdp_'):
        full = os.path.join(scratch, f)
        try:
            if os.path.isfile(full):
                os.remove(full)
                print("Removed:", f)
        except:
            pass

print("Temporary render files cleaned up.")
