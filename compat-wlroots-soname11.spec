#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v4
# autospec commit: da8b975
#
Name     : compat-wlroots-soname11
Version  : 0.16.2
Release  : 21
URL      : https://gitlab.freedesktop.org/wlroots/wlroots/-/archive/0.16.2/wlroots-0.16.2.tar.gz
Source0  : https://gitlab.freedesktop.org/wlroots/wlroots/-/archive/0.16.2/wlroots-0.16.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 MIT
Requires: compat-wlroots-soname11-lib = %{version}-%{release}
Requires: compat-wlroots-soname11-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : clr-hardware-files
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(gbm)
BuildRequires : pkgconfig(libavcodec)
BuildRequires : pkgconfig(libavformat)
BuildRequires : pkgconfig(libavutil)
BuildRequires : pkgconfig(libcap)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libinput)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(libseat)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(pixman-1)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(wayland-server)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : systemd-dev
BuildRequires : xwayland
BuildRequires : xwayland-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# wlroots
Pluggable, composable, unopinionated modules for building a [Wayland]
compositor; or about 60,000 lines of code you were going to write anyway.

%package lib
Summary: lib components for the compat-wlroots-soname11 package.
Group: Libraries
Requires: compat-wlroots-soname11-license = %{version}-%{release}

%description lib
lib components for the compat-wlroots-soname11 package.


%package license
Summary: license components for the compat-wlroots-soname11 package.
Group: Default

%description license
license components for the compat-wlroots-soname11 package.


%prep
%setup -q -n wlroots-0.16.2
cd %{_builddir}/wlroots-0.16.2
pushd ..
cp -a wlroots-0.16.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1708526867
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/compat-wlroots-soname11
cp %{_builddir}/wlroots-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/compat-wlroots-soname11/cf7d4b8dccadb7713df91a14a5d9f5b53f493f3c || :
cp %{_builddir}/wlroots-%{version}/tinywl/LICENSE %{buildroot}/usr/share/package-licenses/compat-wlroots-soname11/df855b408256fed71fe29eb1382d03841508d0f2 || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
## Remove excluded files
rm -f %{buildroot}*/usr/include/wlr/backend.h
rm -f %{buildroot}*/usr/include/wlr/backend/drm.h
rm -f %{buildroot}*/usr/include/wlr/backend/headless.h
rm -f %{buildroot}*/usr/include/wlr/backend/interface.h
rm -f %{buildroot}*/usr/include/wlr/backend/libinput.h
rm -f %{buildroot}*/usr/include/wlr/backend/multi.h
rm -f %{buildroot}*/usr/include/wlr/backend/session.h
rm -f %{buildroot}*/usr/include/wlr/backend/wayland.h
rm -f %{buildroot}*/usr/include/wlr/backend/x11.h
rm -f %{buildroot}*/usr/include/wlr/config.h
rm -f %{buildroot}*/usr/include/wlr/interfaces/wlr_buffer.h
rm -f %{buildroot}*/usr/include/wlr/interfaces/wlr_keyboard.h
rm -f %{buildroot}*/usr/include/wlr/interfaces/wlr_output.h
rm -f %{buildroot}*/usr/include/wlr/interfaces/wlr_pointer.h
rm -f %{buildroot}*/usr/include/wlr/interfaces/wlr_switch.h
rm -f %{buildroot}*/usr/include/wlr/interfaces/wlr_tablet_pad.h
rm -f %{buildroot}*/usr/include/wlr/interfaces/wlr_tablet_tool.h
rm -f %{buildroot}*/usr/include/wlr/interfaces/wlr_touch.h
rm -f %{buildroot}*/usr/include/wlr/render/allocator.h
rm -f %{buildroot}*/usr/include/wlr/render/dmabuf.h
rm -f %{buildroot}*/usr/include/wlr/render/drm_format_set.h
rm -f %{buildroot}*/usr/include/wlr/render/egl.h
rm -f %{buildroot}*/usr/include/wlr/render/gles2.h
rm -f %{buildroot}*/usr/include/wlr/render/interface.h
rm -f %{buildroot}*/usr/include/wlr/render/pixman.h
rm -f %{buildroot}*/usr/include/wlr/render/wlr_renderer.h
rm -f %{buildroot}*/usr/include/wlr/render/wlr_texture.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_buffer.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_compositor.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_cursor.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_damage_ring.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_data_control_v1.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_data_device.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_drm.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_drm_lease_v1.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_export_dmabuf_v1.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_foreign_toplevel_management_v1.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_fullscreen_shell_v1.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_gamma_control_v1.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_idle.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_idle_inhibit_v1.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_idle_notify_v1.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_input_device.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_input_inhibitor.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_input_method_v2.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_keyboard.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_keyboard_group.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_keyboard_shortcuts_inhibit_v1.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_layer_shell_v1.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_linux_dmabuf_v1.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_matrix.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_output.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_output_damage.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_output_layout.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_output_management_v1.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_output_power_management_v1.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_pointer.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_pointer_constraints_v1.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_pointer_gestures_v1.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_presentation_time.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_primary_selection.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_primary_selection_v1.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_region.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_relative_pointer_v1.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_scene.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_screencopy_v1.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_seat.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_server_decoration.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_session_lock_v1.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_single_pixel_buffer_v1.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_subcompositor.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_surface.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_switch.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_tablet_pad.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_tablet_tool.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_tablet_v2.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_text_input_v3.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_touch.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_viewporter.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_virtual_keyboard_v1.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_virtual_pointer_v1.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_xcursor_manager.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_xdg_activation_v1.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_xdg_decoration_v1.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_xdg_foreign_registry.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_xdg_foreign_v1.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_xdg_foreign_v2.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_xdg_output_v1.h
rm -f %{buildroot}*/usr/include/wlr/types/wlr_xdg_shell.h
rm -f %{buildroot}*/usr/include/wlr/util/addon.h
rm -f %{buildroot}*/usr/include/wlr/util/box.h
rm -f %{buildroot}*/usr/include/wlr/util/edges.h
rm -f %{buildroot}*/usr/include/wlr/util/log.h
rm -f %{buildroot}*/usr/include/wlr/util/region.h
rm -f %{buildroot}*/usr/include/wlr/version.h
rm -f %{buildroot}*/usr/include/wlr/xcursor.h
rm -f %{buildroot}*/usr/include/wlr/xwayland.h
rm -f %{buildroot}*/usr/include/wlr/xwayland/server.h
rm -f %{buildroot}*/usr/include/wlr/xwayland/xwayland.h
rm -f %{buildroot}*/usr/lib64/libwlroots.so
rm -f %{buildroot}*/usr/lib64/pkgconfig/wlroots.pc
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libwlroots.so.11
/usr/lib64/libwlroots.so.11

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/compat-wlroots-soname11/cf7d4b8dccadb7713df91a14a5d9f5b53f493f3c
/usr/share/package-licenses/compat-wlroots-soname11/df855b408256fed71fe29eb1382d03841508d0f2