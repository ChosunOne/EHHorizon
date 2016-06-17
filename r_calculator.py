import math


def density(mass, volume):
    return mass / volume

def energyPressure(mass, volume):
    energy = mass * (299792458.0**2)
    return energy / volume

def evansHauman(mass):
    gravity = 6.67408 * 10**-11                             #m^3/(kgs^2)
    light = 299792458.0**2                                  #(m/s)^2
    cosmo = 1 * 10.0**-52 * light                           #1/s^2
    massDensity = 1.0012 * 10.0**-26                        #kg/m^3
    energy = 3.0 * 10.0**52 * light                         #J
    engDensity = energy / (4.0 * 10.0**80)                  #J/m^3
    omega = massDensity + (3.0 * engDensity) / light        #kg/m^3

    denonimator = ((-4.0 * math.pi * gravity)/3.0) * omega + cosmo/3.0
    numerator = gravity * mass
    return (numerator / denonimator)**(1.0/3.0)

massLocalGroup = 2.386 * 10**42 + 2.983 * 10**42

print(evansHauman(massLocalGroup))
    

