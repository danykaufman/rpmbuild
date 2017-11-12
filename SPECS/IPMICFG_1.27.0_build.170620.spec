%define debug_package %{nil}

Summary: SuperMicro IPMI tools
Name: IPMICFG_1.27.0_build.170620
Version: 1
Release: 1
License: GPL
# BuildArch states the intented architecture; in this case we build a package for all.
# if you copy binaries for a specific architecture please state it here
BuildArch: x86_64
Group: Development/Tools
# The name of our source tar.gz file is next, make sure this name is correct. The version number
# does matter a lot!
Source: /root/rpmbuild/SOURCES/IPMICFG_1.27.0_build.170620.tar.gz
BuildRoot: /tmp/IPMICFG

%description
SuperMicro IPMICFG files will be copied to the system

%prep
%setup -n IPMICFG_1.27.0_build.170620/Linux/64bit
# In the prep section the tar.gz file gets unpacked to a directory.
# the directory is

%build
# Normally this part would be full of fancy compile stuff. Make this, make that.
# We simple folks, we just want to copy some files out of a tar.gz.
# so we pass this section with nothing done...

%install
# Installing happens here, normally using the “make install”
# command, it normally places the files
# where they need to go. You can also copy the files, as we do here...

# First we make sure we start clean
rm -rf $RPM_BUILD_ROOT

# Then we create the directories where the files go
# don't worry if the directories exist on your target systems, rpm
# creates if necessary
mkdir -p $RPM_BUILD_ROOT/opt/IPMICFG

# The actual moving
cp * $RPM_BUILD_ROOT/opt/IPMICFG

%files
# The file section, it has to be exact, matching all files.
# Here you have the power to implement all rights, even if they are different in the tar.gz
/opt/IPMICFG/DCMICap.dat
/opt/IPMICFG/GenEvt.dat
/opt/IPMICFG/IPMICFG-Linux.x86_64
/opt/IPMICFG/MBType.dat
/opt/IPMICFG/MRCCode.dat
/opt/IPMICFG/MRCCode2.dat
/opt/IPMICFG/Menu.dat
/opt/IPMICFG/PMBusStatus.dat
/opt/IPMICFG/SpecEvt1.dat
/opt/IPMICFG/SpecEvt2.dat
/opt/IPMICFG/SpecEvt3.dat
/opt/IPMICFG/SpecEvt4.dat
/opt/IPMICFG/SpecEvt5.dat

%clean
rm -rf $RPM_BUILD_ROOT


%changelog
* Mon Oct 2 2017 Dany Kaufman <danyk@iguazio.com> - 1-1
Initial creation
