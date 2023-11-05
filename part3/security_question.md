# Preguntas de seguridad

El top 10 de OWASP 2021 lo componen las siguientes vulnerabilidades, por cada una expongo las acciones que tomaría en el sistema para evitar que se presenten. 

1. **Pérdida de Control de Acceso**:
verificaría el acceso basado en roles otorgando los mínimos permisos necesarios a cada uno.
Por ejemplo que mis 12 ingenieros de software tengan acceso total al sistemas puede no ser necesario e implica demasiados puntos de fallo que podrían comprometer la seguridad del sistema.
También verificaría que se haga uso de contraseñas muy seguras  almacenadas de forma correcta y si es posible que se implemente autenticación de doble factor

1. **Fallas Criptográficas**:
Revisaría que la información sensible tanto en reposo como en transito esté adecuadamente cifrada. por ejemplo utilizando HTTPS para la comunicación y algoritmos de cifrado robustos para contraseñas y datos sensibles.

1. **Inyección**: Utilizaría un ORM cómo SQLModel o SQLAlchemy para minimizar la posibilidad de que se presente SQL Injection, y en caso de que sea necesario hacer queries nativas, sanitizarlas de manera adecuada.

2. **Diseño Inseguro**:
Verificar que se esté utilizando prácticas y patrones de diseño que velen por la seguridad, por ejemplo no exponer directamente las modelos de la base de datos al cliente y en su lugar hacer uso de DTOs que contengan solo la información que es necesaria en el cliente.

1. **Configuración de Seguridad Incorrecta**:
Configuraría la seguridad en los servicios de AWS para restringir el acceso y la comunicación con los servicios.

1. **Componentes Vulnerables y Desactualizados**:Utilizar las ultimas versiones estables de todas las librerías, frameworks y tecnologías utilizados, especialmente si se tienen versiones con vulnerabilidades conocidas. También establecería un proceso de gestión de vulnerabilidades.

2. **Fallas de Identificación y Autenticación**:
Utilizar un procedimiento robusto de autenticación y autorización. Realizaría auditorías de ingresos al sistema para detectar rápidamente posibles fallos en la autenticación y autorización.

1. **Fallas en el Software y en la Integridad de los Datos**: Implementaría un proceso de auditoría que registre los cambios sobre las entidades más críticas de mi base de datos, por ejemplo las relacionadas con ventas, ordenes e inventario.
También verificar que el backend y mi modelo de datos sean lo suficientemente robustos para validar que la información es correcta siempre.

1. **Fallas en el Registro y Monitoreo**:
Monitorearía la infraestructura con herramientas como Prometheus y Grafana. También establecería alertas y realizaría análisis de seguridad de forma regular.

1.  **Falsificación de Solicitudes del Lado del Servidor (A10:2021)**: Verificaría que el sistema se asegure de que todas las solicitudes sean válidas y a recursos permitidos además sanitizarlas cuando sea necesario.


Además, como medida general, me aseguraría de que todo el personal esté adecuadamente capacitado en seguridad informática según su rol y realizaría pruebas de penetración regularmente.
