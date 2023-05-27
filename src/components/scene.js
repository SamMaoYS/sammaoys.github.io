import * as React from 'react';
import { Suspense } from "react"
import { Canvas, useFrame } from "@react-three/fiber"

import Background from './background';

export default function HomeScene() {
  return (
    <Canvas shadows camera={{ position: [0, 1.5, 2.5], fov: 50 }}>
      <ambientLight />
      <directionalLight position={[-5, 5, 5]} castShadow shadow-mapSize={1024} />
      <group rotation={[0.5 * Math.PI, 0, 0]} scale={0.4} position={[0, 0.5, 0]}>
        <Suspense fallback={null}>
          <Background />
        </Suspense>
      </group>
      <mesh rotation={[-0.5 * Math.PI, 0, 0]} position={[0, -1, 0]} receiveShadow>
        <planeBufferGeometry args={[10, 10, 1, 1]} />
        <shadowMaterial transparent opacity={0.2} />
      </mesh>
    </Canvas>
  )
}