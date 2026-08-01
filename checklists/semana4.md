# Checklist de Revisión

- [ ] **Contenerización:** `docker build` y `docker-compose up` funcionan a la primera sin errores de entorno.
- [ ] **Integración Continua (CI):** El pipeline de GitHub Actions está en verde con evidencia de ejecuciones reales, y el badge de estado está visible en el `README.md`.
- [ ] **Despliegue Continuo (CD):** La URL pública está respondiendo correctamente. Un simple push a la rama principal detona un despliegue automático.
- [ ] **Seguridad y Documentación:** No hay ningún secreto o credencial expuesta en el historial de Git. El archivo `AI_LOG.md` está actualizado.
- [ ] **Dominio del Sistema:** El autor puede explicar cada línea de su `Dockerfile` y de su archivo `ci.yml`, así como la estrategia para realizar un *rollback* (reversión) en producción.