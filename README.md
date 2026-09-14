# E-commerce Starter

## Services
- **Frontend**: Vanilla JavaScript + Vite 7.3.6 (Port 5173)
- **Products**: PHP 8.4 + Slim 4.15.3 (Port 8082)
- **Users**: Python 3.13 + FastAPI 0.141.1 (Port 8000)
- **Orders**: Java 25 + Spring Boot 4.1.1 (Port 8083)
- **Database**: PostgreSQL 18.6 (Port 5432)
- **Migrations**: Node.js 24 + Prisma 7.10.0

## Quick Start
1. **Configure**: `cp .env.example .env`
2. **Run**: `docker-compose up --build`

## Structure
- `frontend/`: UI application (Vanilla JavaScript)
- `products-service/`: Product catalog API (PHP)
- `users-service/`: User management API (Python)
- `orders-service/`: Order management API (Java)
- `database/`: Prisma migrations

## Documentation
- [Development Setup Guide](dev-starter.md) - **Start here for new developers**
- [Architecture Overview](ARCHITECTURE.md)
- [Frontend Conversion Plan](plans/frontend-vanilla-js-conversion.md)
