import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="The Crystal of Ulumok",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["map.jpg", "tavern.jpg",
                                            "KnightAttck.png", "KnightDeath.png","KnightWalk.png",
                                            "WizardAttack.png", "WizardDeath.png","WizardWalk.png",
                                            "EnemyAttack.png", "EnemyDeath.png","EnemyWalk.png",
                                            "spell.png", "crystal.png", "scores.txt",
                                            "theme.mp3", "enemyDeath.wav", "SwordSound.mp3", "spellSound.mp3",
                                            "itemGem.png"]}},
    executables = executables

    )
