package dataProcessing

import (
	"api/database/services"
	"api/grpcGeneratedCode"
	"api/interop"
	"api/model/dataset"
)

func Compute(data dataset.Dataset) error {
	ch := make(chan *grpcGeneratedCode.DatasetResponse)
	target := "localhost:1111"
	go interop.SendRequest(data.Data, target, ch)

	datasetProcessed := <-ch

	metadata := &dataset.Metadata{
		Transactions: datasetProcessed.GetTransactions(),
		DatasetID:    data.ID,
		UserID:       data.UserID,
	}

	services.CreateMetadata(metadata)

	return nil
}
