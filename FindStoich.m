%FindStoich
%M Hageman 11/2018

% The Cantera commands......
%>> set(g,'T',1500,'P',oneatm,'X',ones(nSpecies(g),1));
%>> nu_r   = stoich_r(g)    % reactant stoichiometric coefficient mstix
%.....may do the same thing as this function. see https://cantera.org/tutorials/matlab-tutorial.html

%Inputs
%Species = {'CH4' 'O2' 'N2'}
%MolesInertperMoleOxidizer - as in Air = O2 +3.76N2

%Outputs
%OF_Stoich - mass-based stoichiometric Oxidizer to fuel ratio
%Inert %considered part of oxidizer - as in Air = O2 +3.76N2

%Uses Functions
%CHON_MW.m
%....ParseElementString.m


function [OF_Stoich, Molarray] = FindStoich(Species, MolesInertperMoleOxidizer)

%CHON = {'C' 'H' 'O' 'N' 'Ar' 'He'};
Fuel = char(Species(1));
Oxidizer=char(Species(2));
if length(Species)==3
    Inert=char(Species(3));
else
    Inert=char(0);
end

%Parse Fuel String
[FuelEleList FuelNumList]=ParseElementString(Fuel);
[~,FindC]=ismember(FuelEleList,'C');
[~,FindH]=ismember(FuelEleList,'H');
[~,FindO]=ismember(FuelEleList,'O');
[~,FindN]=ismember(FuelEleList,'N');
FuelCarbon=sum(FindC.*FuelNumList);
FuelHydrogen=sum(FindH.*FuelNumList);
FuelOxygen=sum(FindO.*FuelNumList);
FuelNitrogen=sum(FindN.*FuelNumList);
[FuelMW] = CHON_MW(Fuel);

%Parse Oxidizer String
[OxEleList OxNumList]=ParseElementString(Oxidizer);
[~,FindH]=ismember(OxEleList,'H');
[~,FindO]=ismember(OxEleList,'O');
[~,FindN]=ismember(OxEleList,'N');
OxidizerHydrogen=sum(FindH.*OxNumList);
OxidizerOxygen=sum(FindO.*OxNumList);
OxidizerNitrogen=sum(FindN.*OxNumList);
[OxidizerMW] = CHON_MW(Oxidizer);

%Inert String is irrelevant.  Only need MW.
[InertMW] = CHON_MW(Inert);

%Stoichiometric Equations
%CxHyOz +a(Ov+Nw)->(n1)CO2+(n2)H2O+(n3)N2
x=FuelCarbon;
y=FuelHydrogen;
z=FuelOxygen; 
w=OxidizerNitrogen;
v=OxidizerOxygen;

n1=x;
n2=y/2;
a=((2*n1)+n2-z)/v;

MolesFuel=1;
MolesOxidizer=a;
MolesInert=a*MolesInertperMoleOxidizer;
Molarray=[MolesFuel MolesOxidizer MolesInert];

OF_Stoich = (a*(OxidizerMW+MolesInertperMoleOxidizer*InertMW))/(FuelMW);
