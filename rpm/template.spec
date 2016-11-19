Name:           ros-jade-csapex
Version:        0.9.3
Release:        0%{?dist}
Summary:        ROS csapex package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ra.cs.uni-tuebingen.de/forschung/apex/
Source0:        %{name}-%{version}.tar.gz

Requires:       mesa-libGL-devel
Requires:       mesa-libGLU-devel
Requires:       qt5-qtbase
Requires:       qt5-qtbase-gui
Requires:       ros-jade-class-loader
Requires:       tinyxml-devel
Requires:       yaml-cpp-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  qt5-qtbase
BuildRequires:  qt5-qtbase-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-class-loader
BuildRequires:  tinyxml-devel
BuildRequires:  yaml-cpp-devel

%description
The csapex package provides a gui for prototyping algorithms and experimenting

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Sat Nov 19 2016 buck <sebastian.buck@uni-tuebingen.de> - 0.9.3-0
- Autogenerated by Bloom

* Fri Nov 18 2016 buck <sebastian.buck@uni-tuebingen.de> - 0.9.2-0
- Autogenerated by Bloom

* Fri Nov 18 2016 buck <sebastian.buck@uni-tuebingen.de> - 0.9.1-0
- Autogenerated by Bloom

