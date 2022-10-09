# Copyright (C) 2022 l.pierfederici@tudenti.unipi.it

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import math

class Particle:
    """Class representing a generic particle.
    """
    def __init__(self, name, mass, charge, momentum = 0.):
        """Arguments (units c=1) :
        name = particle name
        mass = mass in MeV
        charge = charge in unit of e
        momentum = module of the momentum in MeV
        """
        self.name = name
        self.mass = mass 
        self.charge = charge
        self.momentum = momentum #chiamata al property setter che inizializza l'attributo ._momentum
                                 #se mettessi subito ._momentum l'utente potrebbe assegnare direttamente (senza property setter) valori negativi
    def info(self):
        """Prints some info about the particle.
        """
        msg = 'Particle {} of mass : {:.3f} MeV and charge {}'
        return msg.format(self.name, self.mass, self.charge)
    
    @property
    def energy(self):
        """Particle energy in MeV.
        """
        return math.sqrt(self.mass**2 + self.momentum**2)
    
    @energy.setter
    def energy(self, energy):
        """Set the particle energy. It allows to set particle.energy = x.
        Formally there's no energy attribute; I have to change the momentum value.
        """
        if energy < self.mass:
            print('Cannot set an energy value lower than the particle mass')
        else:
            self.momentum = math.sqrt(energy**2 - self.mass**2)

    @property
    def momentum(self):
        """Set the particle momentum. It cannot accept negative values.
        """
        return self._momentum

    @momentum.setter 
    def momentum(self, momentum):
        if momentum < 0:
            print('Cannot set a negative momentum value')
            print('Momentum will be set to 0.')
            self._momentum = 0.
        else:
            self._momentum = momentum


proton = Particle('Proton', 938., +1, -20)

