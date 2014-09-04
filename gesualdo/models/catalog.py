from django.db import models


class Catalog(models.Model):
    class Meta:
        app_label="gesualdo"
        unique_together = ('choice_catalog', 'identifier',)

    RISM_A = 'RISM_A'
    RISM_B = 'RISM_B'
    CENSUS = 'CENSUS'
    VOGEL = 'VOGEL'
    BROWN = 'BROWN'
    HEARTZ = 'HEARTZ'
    VANHULST = 'VANHULST'
    LESURE = 'LESURE'
    POGUE = 'POGUE'
    AGEE = 'AGEE'
    BERNSTEIN = 'BERNSTEIN'
    BOETTICHER = 'BOETTICHER'
    BOORMAN = 'BOORMAN'
    GUILLO = 'GUILLO'
    LEWIS = 'LEWIS'
    SARTORI = 'SARTORI'
    WEAVER = 'WEAVER'
    PATALAS ='PATALAS'
    GOOVEARTS = 'GOOVEARTS'

    CHOICE_CATALOG = (
        (RISM_A, 'Rism A'),
        (RISM_B, 'Rism B'),
        (CENSUS,'Census'),
        (VOGEL,'Vogel'),
        (BROWN,'Brown'),
        (HEARTZ,'Hearz'),
        (VANHULST,'Vanhulst'),
        (LESURE,'Lesure'),
        (POGUE,'Pogue'),
        (AGEE,'Agee'),
        (BERNSTEIN,'Bernstein'),
        (BOETTICHER,'Boetticher'),
        (BOORMAN,'Boorman'),
        (GUILLO,'Guillo'),
        (LEWIS,'Lewis'),
        (SARTORI,'Sartori'),
        (WEAVER,'Weaver'),
        (PATALAS, 'Patalas'),
        (GOOVEARTS, 'Goovearts'),
    )


    choice_catalog = models.CharField(max_length=10, choices=CHOICE_CATALOG, default=RISM_A )
    identifier = models.CharField(max_length=32, blank=True, null=True)
    n_pdf = models.CharField(max_length=32, blank=True, null=True)
    n_mf = models.CharField(max_length=32, blank=True, null=True)



    def __unicode__(self):
        return u"{0}, ({1})".format(self.identifier, self.choice_catalog)

    def cote(self):
        return u"{0} : {1}".format(self.choice_catalog, self.identifier)