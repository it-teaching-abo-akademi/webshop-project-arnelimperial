import React from "react";
import Particles from "react-particles-js";
import './style.css';
const ParticleComponent = () => (
  <div className="wrapper">
    <Particles
      params={{
        particles: {
          line_linked: {
            shadow: {
              enable: true,
              color: "#3CA9D1",
              blur: 5,
            },
          },
        },
      }}
     
    />
    <div className="text">
      <h1 className="text-white">This is a test</h1>
    </div>
  </div>
);

export default ParticleComponent;
