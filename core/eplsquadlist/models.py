from django.db import models

class EPL(models.Model):
    class EPLTeams(models.TextChoices):
        ARSENAL = "Arsenal"
        ASTONVILLA = "AstonVilla"
        BOURNEMOUTH = "Bournemouth"
        BRENTFORD = "Brentford"
        BRIGHTON = "Brighton"
        BURNLEY = "Burnley"
        CHELSEA = "Chelsea"
        CRYSTALPALACE = "CrystalPalace"
        EVERTON = "Everton"
        FULHAM = "Fulham"
        LIVERPOOL = "Liverpool"
        LUTON = "Luton"
        MANCHESTERCITY = "ManchesterCity"
        MANCHESTERUNITED = "ManchesterUnited"
        NEWCASTLEUNITED = "NewcastleUnited"
        NOTTINGHAMFOREST = "NottingHamForest"
        SHIEFFIELDUNITED = "ShieffieldUnited"
        TOTTENHAMHOTSPUR = "TottenhamHotspur"
        WESTHAM = "WestHam"
        WOLVES = "Wolves"
    
    Position = models.CharField(max_length=256)
    Team = models.CharField(max_length=256, choices=EPLTeams.choices)
    Nation = models.CharField(max_length=256)
    PlayerName = models.CharField(max_length=256)
    def __str__(self):
        return(self.Position)
        return(self.Team)
        return(self.Nation)
        return(self.PlayerName)
        
        


    
  

