import { Controller, Get, Logger, Query } from '@nestjs/common';
import { ConsumptionService } from './consumption.service';

@Controller('/predict/consumption')
export class ConsumptionController {
  private logger = new Logger('ConsumptionController');
  constructor(private consumptionService: ConsumptionService) {}

  @Get()
  async getConsumption() {
    this.logger.verbose(`getConsumption trying to get consumption`);
    const result = await this.consumptionService.getConsumption();
    return result;
  }
}
