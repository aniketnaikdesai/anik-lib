def check_file_exist(f,p=""):
    from pathlib import Path
    if not (p and p.strip()):
        config = Path(str(Path.cwd()).replace('\\', '/')+'/'+f)
    else:
        config = Path(p+'/'+f)
    if config.is_file():
        return True
    else:
        return False