with import <nixpkgs> {};
stdenv.mkDerivation rec {
  name = "OpenWeather for location";
  src = "./src";
  env = buildEnv { name = name; paths = buildInputs; };
  buildInputs = [
    git
    texlive.combined.scheme-small
    pandoc
    gawk
    python310
    python310Packages.requests
    python310Packages.aiohttp
  ];
}
