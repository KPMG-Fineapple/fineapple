import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { PowerGenerationModule } from './power-generation/power-generation.module';
import { ConsumptionModule } from './consumption/consumption.module';

@Module({
  imports: [ConfigModule.forRoot(), PowerGenerationModule, ConsumptionModule],
})
export class AppModule {}
