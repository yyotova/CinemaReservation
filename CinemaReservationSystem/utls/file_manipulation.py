def write_file(file, info):
    file = open(file, "a")
    file.write(f'{info}\n')
    file.close()
