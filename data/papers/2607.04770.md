# Cam2Sim: Neural Scenario Reconstruction for Closed-Loop Autonomous Driving Simulation

- arXiv ID: `2607.04770v1`
- Authors: Davide Jannussi, Stefano Carlo Lambertenghi, Constantin Carste, Andrea Stocco
- Published: 2026-07-06
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.04770v1) | [pdf](https://arxiv.org/pdf/2607.04770v1)

## Abstract

Simulation-based testing enables safe and repeatable evaluation of autonomous driving systems, but its effectiveness is limited by the gap between synthetic simulator outputs and real-world camera observations. To address this problem, we present Cam2Sim, a tool that transforms real-world driving recordings into playable CARLA simulation scenarios. Starting from camera images and poses, Cam2Sim reconstructs road geometry, ego trajectories, parked vehicles, and simulation assets, and augments the reconstructed environment with Gaussian Splatting to render camera observations that resemble the original recording. The framework supports ROS-based data extraction, parked-vehicle detection, OpenStreetMap-based map generation, CARLA scenario construction, Gaussian Splatting training, trajectory replay, and closed-loop execution with a system under test. We validate Cam2Sim on a real-world urban-driving scenario with a camera-based end-to-end driving model, comparing reconstruction quality, image-generation quality, and closed-loop behavior against both a simulation-only baseline and the real-world target. Results show that Gaussian-Splatting-based rendering reduces the visual gap with respect to standard simulator rendering and improves behavioral similarity to the real-world reference runs. The artifact is publicly available at https: //github.com/ast-fortiss-tum/cam2sim, and a screencast showing the tool is available at https://youtu.be/KmZ74l1__lI
