import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { PowerGenerationModule } from './power-generation/power-generation.module';
import { ConsumptionModule } from './consumption/consumption.module';
import { InvestModule } from './invest/invest.module';

@Module({
  imports: [ConfigModule.forRoot(), PowerGenerationModule, ConsumptionModule, InvestModule],
})
export class AppModule {}
