import cx_Freeze
executables=[cx_Freeze.Executable("race.py")]
cx_Freeze.setup(name="A bit Racey",
                options={"build_exe":{"packages":["pygame"],
                                      "include_files":["car.png"]}},
                executables=executables)
